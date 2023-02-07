n=int(input())
i=0
while i**2<n:
    print(i**2, sep=" ", end=" ")
    i+=1


i=2
n=int(input())
while i<=n:
    if n%i!=0:
        print(i)
        break
    i+=1


i=1
n=int(input())
a=2
while a<=n:
    a*=2
    i+=1
print(i-1, a//2)


n=int(input())
i=0
y=int(input())
while n<y:
    n+=n*0.1
    i+=1
print(i+1)


i=0
while True:
    A=int(input())
    if A==0:
        print(i)
        break
    i+=1


s=0
i=0
while True:
    A=int(input())
    if A==0:
        print(s/i)
        break
    s+=A
    i+=1


s=0
i=0
k=0
while True:
    A=int(input())
    if A==0:
        print(k-1)
        break
    i+=1
    if s<A:
        s=A
        k=i


s=0
B=0
while True:
    A=int(input())
    if A==0:
        print(s-1)
        break
    if A>B:
        s+=1
    B=A



m=[]
while True:
    A=int(input())
    if A==0:
        break
    m.append(A)
m=m.sort()
k=len(m)
print(m[k-1])


m=[]
while True:
    A=int(input())
    if A==0:
        break
    m.append(A)
m=m.sort()
print(m.count(m[-1]))


A=int(input())
a=0
b=1
c=1
for i in range(2,A):
    k=c
    c=b+c
    a=b
    b=k
print(c)


A=int(input())
a, b, c=0, 1, 1
i=2
if A==a:
    print(0)
elif A==b:
    print('1 or 2')
elif A==c:
    print('1 or 2')
else:
    while A>c:
        i+=1
        k=c
        c=b+c
        a=b
        b=k
if c==A:
    print(i)
else:
    print(-1)


k, s=1, 0
B=0
while True:
    A=int(input())
    if A==0:
        if k>s:
            s=k
        break
    if A==B:
        k+=1
    else:
        if k>s:
            s=k
        k=1
    B=A
print(s)


i, s, t =0, 0, 0
a=[]
while True:
    A=int(input())
    if A==0:
        break
    s+=A
    i+=1
    a.append(A)
s=s/i
for j in range(len(a)):
    t+=(a[j]-s)**2
t=(t/(i-1))**0.5
print(t)