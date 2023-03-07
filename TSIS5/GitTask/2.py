import re

st='qwesdfadfgb'
x=re.search(r'.*a+(b.*){2}(b.*)?.*', st)
if x!=-1:
    print('Exist')
else:
    print('None')