import json, re, os, glob, sys
BANKS="/Users/admin/Documents/2026/Snuffy-Book/BANKS"
CANON="/Users/admin/Documents/2026/Snuffy-Book/SNUFFY-CANON-EDITION-4.2-WORKING-2026-10-25/lean/Snuffy"
def decls(text):
    text=re.sub(r"/-.*?-/","",text,flags=re.S); text=re.sub(r"--[^\n]*","",text)
    out={}
    for mt in re.finditer(r"(?m)^\s*(?:@\[[^\]]*\]\s*)?(?:private\s+|protected\s+)?(theorem|lemma)\s+(\S+)(.*?)(?=:=)",text,flags=re.S):
        name=mt.group(2).split(".")[-1]; stmt=" ".join(mt.group(3).split())
        out.setdefault(name,[]).append(stmt)
    return out
canon={}
for f in glob.glob(CANON+"/*.lean"):
    for n,ss in decls(open(f).read()).items():
        for s in ss: canon.setdefault(n,[]).append((os.path.basename(f),s))
d=json.load(open(sys.argv[1]))
res=[]
for it in d["files"]:
    if it["status"]!="content_comparison_pending": continue
    p=os.path.join(BANKS,it["path"])
    if not os.path.exists(p): res.append((it["path"],"MISSING",[],[],[])); continue
    ds=decls(open(p).read())
    same=[];var=[];absent=[]
    for n,ss in ds.items():
        for s in ss:
            if n not in canon: absent.append(n)
            elif any(s==cs for _,cs in canon[n]): same.append(n)
            else: var.append((n,[m for m,_ in canon[n]]))
    res.append((it["path"],"A" if not var and not absent else ("C" if absent else "B"),same,var,absent))
json.dump(res,open(sys.argv[2],"w"),indent=1)
from collections import Counter
print(Counter(r[1] for r in res))
for r in res:
    if r[1]!="A": print(r[1], r[0], "same",len(r[2]),"var",[v[0] for v in r[3]][:6],"absent",r[4][:8])
