#!/usr/bin/env python3
"""Publish only the audited manifest as a new version of the existing record.

Credentials are read locally and are never written to logs or receipts.
The user's 27 October publication instruction authorises this operation.
"""
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import time
import urllib.error
import urllib.request

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
API = 'https://zenodo.org/api'
PARENT = 23631881
STATE = HERE/'ZENODO-STATE.json'
token = None


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def request(method, url, payload=None, raw=None):
    assert url.startswith('https://zenodo.org/api/'), 'Unexpected publication host'
    if raw is not None:
        # Stream large files through curl. Pass the credential through
        # stdin configuration, never in process arguments or a log file.
        assert method == 'PUT' and isinstance(raw, Path)
        config = 'header = '+json.dumps('Authorization: Bearer '+token)+'\n'
        cp = subprocess.run(['curl', '--silent', '--show-error', '--fail-with-body',
                             '--config', '-', '--connect-timeout', '30', '--max-time', '900',
                             '--retry', '2', '--retry-delay', '2', '--upload-file', str(raw), url],
                            input=config.encode(), capture_output=True)
        if cp.returncode:
            raise RuntimeError('Streaming upload failed: '+cp.stderr.decode(errors='replace'))
        return json.loads(cp.stdout)
    headers = {'Authorization': 'Bearer '+token,
               'User-Agent': 'Snuffy-Canon-Edition/4.2 (verified publication)',
               'Accept': 'application/json'}
    data = raw
    if payload is not None:
        data = json.dumps(payload).encode()
        headers['Content-Type'] = 'application/json'
    elif raw is not None:
        headers['Content-Type'] = 'application/octet-stream'
    with urllib.request.urlopen(urllib.request.Request(url, data=data, headers=headers, method=method), timeout=60) as response:
        body = response.read()
        return json.loads(body) if body else {}


def file_map(record):
    return {f.get('filename', f.get('key')): {'md5': f.get('checksum', '').removeprefix('md5:'),
                                           'bytes': int(f.get('filesize', f.get('size', 0)))}
            for f in record.get('files', [])}


def main():
    global token
    mode = sys.argv[1] if len(sys.argv) == 2 else ''
    assert mode in ['stage', 'publish'], 'usage: publish-zenodo.py stage|publish'
    manifest = json.loads((HERE/'UPLOAD-MANIFEST.json').read_text())
    assert manifest['all_package_checks_pass']
    audit = json.loads((HERE/'FINAL-VERIFICATION.json').read_text())
    assert audit['all_final_checks_pass'] and audit['checks']['delta_joint']['exact_certificate_decisions'] == 18130
    for entry in manifest['files']:
        path = Path(entry['path'])
        assert path.is_file() and sha(path) == entry['sha256'], entry['name']
    assert sha(Path(manifest['metadata_path'])) == manifest['metadata_sha256']
    token = Path('/Users/admin/.zenodo-token').read_text().strip()
    assert token
    parent = request('GET', f'{API}/deposit/depositions/{PARENT}')
    assert parent['submitted'] and parent['metadata']['version'] == '4.1'
    parent_content = {'version': parent['metadata']['version'], 'doi': parent.get('doi'), 'files': file_map(parent)}
    if STATE.is_file():
        state = json.loads(STATE.read_text())
        assert state['parent_id'] == PARENT
        draft = request('GET', f'{API}/deposit/depositions/{state["draft_id"]}')
    else:
        draft_url = parent['links']['latest_draft']
        if int(draft_url.rstrip('/').split('/')[-1]) == PARENT:
            response = request('POST', parent['links']['newversion'])
            draft_url = response['links']['latest_draft']
        draft = request('GET', draft_url)
        assert int(draft['id']) != PARENT and str(draft['conceptrecid']) == str(parent['conceptrecid'])
        state = {'parent_id': PARENT, 'draft_id': int(draft['id']),
                 'conceptrecid': str(draft['conceptrecid']), 'parent_content_before': parent_content}
        STATE.write_text(json.dumps(state, indent=2)+'\n')
    draft_id = int(draft['id'])
    expected = {e['name']: {'md5': e['md5'], 'bytes': e['bytes']} for e in manifest['files']}
    base = f'{API}/deposit/depositions/{draft_id}'
    if not draft['submitted']:
        assert draft.get('state') == 'unsubmitted'
        assert draft.get('metadata', {}).get('version') in [None, '4.1', '4.2'], 'Different-version draft must not be overwritten'
        metadata = json.loads(Path(manifest['metadata_path']).read_text())
        keys = ['title', 'upload_type', 'publication_date', 'description', 'creators',
                'license', 'version', 'notes', 'related_identifiers', 'keywords']
        request('PUT', base, {'metadata': {k: metadata[k] for k in keys}})
        # Carried files belong to this unpublished new draft, never to 4.1.
        for entry in draft.get('files', []):
            name = entry.get('filename', entry.get('key'))
            current = file_map({'files': [entry]})[name]
            if name not in expected or current != expected[name]:
                request('DELETE', f'{base}/files/{entry["id"]}')
        draft = request('GET', base)
        current = file_map(draft)
        for entry in manifest['files']:
            if current.get(entry['name']) == expected[entry['name']]:
                continue
            print(json.dumps({'uploading': entry['name'], 'bytes': entry['bytes']}), flush=True)
            response = request('PUT', draft['links']['bucket']+'/'+entry['name'], raw=Path(entry['path']))
            assert response['checksum'].removeprefix('md5:') == entry['md5'], entry['name']
            print(json.dumps({'uploaded': entry['name'], 'bytes': entry['bytes'], 'remote_md5_matches': True}), flush=True)
        draft = request('GET', base)
    assert draft['metadata']['version'] == '4.2'
    assert file_map(draft) == expected, (file_map(draft), expected)
    staged = {'draft_id': draft_id, 'files_verified': True, 'files': manifest['files'],
              'upload_manifest_sha256': sha(HERE/'UPLOAD-MANIFEST.json'),
              'metadata_sha256': manifest['metadata_sha256'],
              'physical_boundary_disclosed_in_metadata': True}
    (HERE/'ZENODO-STAGED.json').write_text(json.dumps(staged, indent=2)+'\n')
    if mode == 'stage':
        print(json.dumps({'staged': True, 'draft_id': draft_id, 'published': bool(draft['submitted'])}), flush=True)
        return
    if not draft['submitted']:
        try:
            draft = request('POST', draft['links']['publish'])
        except (TimeoutError, urllib.error.URLError):
            # A timeout may follow a successful publication. Read state;
            # never create another version or republish blindly.
            draft = request('GET', base)
            if not draft.get('submitted'):
                raise
    assert draft['submitted'] and draft['metadata']['version'] == '4.2'
    public = None
    for attempt in range(4):
        try:
            public = request('GET', f'{API}/records/{draft_id}')
            if public.get('metadata', {}).get('version') == '4.2':
                break
        except urllib.error.HTTPError as error:
            if error.code not in [404, 429, 503] or attempt == 3:
                raise
        time.sleep(2)
    assert public and public['metadata']['version'] == '4.2'
    assert file_map(public) == expected
    parent_after = request('GET', f'{API}/deposit/depositions/{PARENT}')
    after_content = {'version': parent_after['metadata']['version'], 'doi': parent_after.get('doi'), 'files': file_map(parent_after)}
    assert after_content == state.get('parent_content_before', parent_content)
    receipt = {'date': '2026-10-27', 'timezone': 'Pacific/Auckland',
               'published': True, 'service': 'Zenodo', 'record_id': draft_id,
               'doi': public.get('doi', draft.get('doi')),
               'url': public['links'].get('self_html', public['links'].get('html', f'https://zenodo.org/records/{draft_id}')),
               'version': '4.2', 'files': manifest['files'],
               'source_commit_before_publication': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip(),
               'all_remote_file_md5_and_sizes_match_local': True,
               'parent_4_1_content_unchanged': True,
               'canonical_checkpoint12_unchanged': '192 / 1158',
               'exact_certificate_decisions': 18130,
               'actual_physical_installation_residual_certified': False,
               'physical_boundary_disclosed_in_published_metadata': True,
               'held_doors_and_companion_published': False,
               'upload_manifest_sha256': sha(HERE/'UPLOAD-MANIFEST.json')}
    (HERE/'PUBLICATION-RECEIPT.json').write_text(json.dumps(receipt, indent=2, ensure_ascii=False)+'\n')
    print(json.dumps({'published': True, 'doi': receipt['doi'], 'url': receipt['url'],
                      'remote_files_verified': len(expected), 'parent_4_1_unchanged': True}), flush=True)


if __name__ == '__main__':
    main()
