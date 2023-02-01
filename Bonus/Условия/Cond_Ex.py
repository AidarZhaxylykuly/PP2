x=int(input())
y=int(input())
if x>y:
    print(y)
else:
    print(x)



x=int(input())
if x>0:
    print(1)
elif x==0:
    print(0)
else:
    print(-1)


x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
if abs(x1-x2)%2==0:
    if abs(y2-y1)%2==0:
        print("YES")
    else:
        print("NO")
else:
    if abs(y2-y1)%2!=0:
        print("YES")
    else:
        print("NO")



x=int(input())
if x%4==0 and x%100!=0 or x%400==0:
    print("YES")
else:
    print("NO")


A=[]
for i in range(3):
    x=int(input())
    A.append(x)
A=sorted(A)
print(A[0])


A.clear()
z=1
for i in range(3):
    x=int(input())
    A.append(x)
if(A[0]==A[1]):
    z+=1
if(A[0]==A[2]):
    z+=1
if(A[1]==A[2]):
    z+=1
if z==4:
    print(3)
else:
    print(z)


x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
if x1==x2:
    print('YES')
else:
    if y1==y2:
        print('YES')
    else:
        print("NO")



x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
if abs(x1-x2)==1:
    print('YES')
else:
    if abs(y1-y2)==1:
        print('YES')
    else:
        print("NO")


x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
if abs(x1-x2)==abs(y1-y2):
    print('YES')
else:
    print('NO')


x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
if x1==x2 or abs(x1-x2)==abs(y1-y2):
    print('YES')
else:
    if y1==y2:
        print('YES')
    else:
        print("NO")


x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
if abs(x1-x2)==2:
    if abs(y1-y2)==1:
        print("YES")
    else:
        print("NO")
elif abs(y1-y2)==2:
    if abs(x1-x2)==1:
        print('YES')
    else:
        print("NO")
else:
    print("NO")


x=int(input())
y=int(input())
z=int(input())
if x*y<z:
    print('NO')
elif (x*y-z)%x==0 or (x*y-z)%y==0:
    print("YES")
else:
    print("NO")



x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
if x1//2<x2:
    if y1//2<y2:
        if x1-x2<y1-y2:
            print(x1-x2)
        else:
            print(y1-y2)
    else:
        if x1-x2>y2:
            print(y2)
        else:
            print(x1-x2)
else:
    if y1//2<y2:
        if x2<y1-y2:
            print(x2)
        else:
            print(y1-y2)
    else:
        if y2<x2:
            print(y2)
        else:
            print(x2)