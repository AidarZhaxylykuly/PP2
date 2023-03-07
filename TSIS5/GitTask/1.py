import re, row

st=row.y
x=re.search(r'.*a+b*.*', st)
if x!=-1:
    print('Exist')
else:
    print('None')