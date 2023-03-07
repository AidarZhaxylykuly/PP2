import re, row

st=row.y
x=re.findall(r'.*([A-Z]{1}.*)+', st)
print(x)