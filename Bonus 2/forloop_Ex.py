A=int(input())
B=int(input())
for i in range(A, B+1):
    print(i)


A=int(input())
B=int(input())
if A<B:
    for i in range(A, B+1):
        print(i)
else:
    for i in range(B, A+1):
        print(i)

    
A=int(input())
B=int(input())
if A%2==0 and A>0:
    A-=1
elif A%2==0 and A<0:
    A+=1
for i in range(A, B-1, -2):
    print(i)


S=0
for i in range(10):
    A=int(input())
    S+=A
print(S)


S=0
N=int(input())
for i in range(N):
    A=int(input())
    S+=A
print(S)


S=0
N=int(input())
for i in range(N):
    S+=i**3
print(S)


S=0
N=int(input())
for i in range(N):
    S*=i
print(S)


S1=0
S=0
N=int(input())
for i in range(N):
    for i in range(N):
        S*=i
    S1+=S
print(S1)


S=0
N=int(input())
for i in range(N):
    A=int(input())
    if A==0:
        S+=1
print(S)


N=int(input())
for i in range(1, N+1):
    for j in range(1, i+1):
        print(j, sep="", end="")
    print()


N=int(input())
A=[]
for i in range(N-1):
    B=int(input())
    A.append(B)
for i in range(1, N+1):
    if i not in A:
        print(i)
        break