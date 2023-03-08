l = [int(a) for a in input().split()]
x=tuple(l)
ind=0
for i in range(len(x)):
    if x[i]:
        continue
    else:
        ind=1
        break
if ind==0:
    print(True)
else:
    print(False)