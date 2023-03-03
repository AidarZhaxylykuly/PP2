def gen(N):
    A=[]
    for i in range(0,N):
        if i%3==0 and i%4==0:
            A.append(i)
    return A
A=gen(int(input()))
B=iter(A)
for i in range(len(A)):
    print(next(B), sep=" ", end=" ")