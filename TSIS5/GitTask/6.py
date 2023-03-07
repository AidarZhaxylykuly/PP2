import re, row

st=row.y
x=re.sub(' ', ':', st)
x=re.sub('.', ':', st)
x=re.sub(',', ':', st)
print(x)