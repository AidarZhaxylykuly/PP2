
def gen(N):
    A=[]
    for i in range(N+1, 0, -1):
        A.append(i)
    return A
A=gen(int(input()))
B=iter(A)
for i in range(len(A)):
    print(next(B), sep=' ', end=' ')