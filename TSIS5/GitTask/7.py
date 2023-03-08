import re

st='qwe_1we_qwe'
s=[]
for i in range(len(st)):
    q=st.find('_')
    if q!=-1:
        st=re.sub('_','', st, 1)
        if st[q].isalpha():
            st=st[:q]+st[q].upper()+st[q+1:]
    else:
        break
print(st)
'''st='qwe_1we_qwe'
x = re.sub(r"_[a-z]", "\1".upper(), st)
print(x)'''
