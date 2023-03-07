import re, row

st=row.y
x=re.findall(r'[a-z]+(_[a-z]+)+', st)
print(x)