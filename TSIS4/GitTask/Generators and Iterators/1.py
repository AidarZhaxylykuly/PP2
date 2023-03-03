def gen(N):
    A=[]
    for i in range(0,N):
        if i**2<=N:
            A.append(i**2)
    return A
A=gen(int(input()))
B=iter(A)
for i in range(len(A)):
    print(next(B))