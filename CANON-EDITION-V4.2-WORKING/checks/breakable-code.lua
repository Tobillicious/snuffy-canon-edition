-- PDF only: let long inline code (hashes, theorem names) break between characters.
local esc = {['\\']='\\textbackslash{}', ['{']='\\{', ['}']='\\}', ['_']='\\_', ['^']='\\^{}',
             ['#']='\\#', ['$']='\\$', ['%']='\\%', ['&']='\\&', ['~']='\\textasciitilde{}'}
function Code(el)
  if not FORMAT:match('latex') or utf8.len(el.text) <= 16 then return nil end
  local parts = {}
  for _, c in utf8.codes(el.text) do
    local ch = utf8.char(c)
    parts[#parts + 1] = esc[ch] or ch
  end
  return pandoc.RawInline('latex', '\\texttt{' .. table.concat(parts, '\\allowbreak{}') .. '}')
end
