import re

st='qweQweQwe'
for i in range(len(st)):
    q=re.search(r'[A-Z]', st)
    if q:
        st=st[: q.start()]+'_'+st[q.start()].lower()+st[q.start()+1:]
    else:
        break
print(st)
'''x=re.findall(r'[A-Z][a-z]*[a-z]$', st)
print(x)'''