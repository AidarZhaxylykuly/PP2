s=input().split()
u=0
l=0
for i in s:
    if i[0].isupper():
        u+=1
    else:
        l+=1
print(u, l)