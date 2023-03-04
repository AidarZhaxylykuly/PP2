import re

st='qwaesdfabbb'
x=re.search(r'.*a+bb(b?).*', st)
print(x)