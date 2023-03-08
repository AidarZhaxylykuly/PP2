l = [int(a) for a in input().split()]
s=1
for i in range(len(l)):
    s*=l[i]
print(s)