def gen(A, B):
    k=[]
    for i in range(A,B+1):
        k.append(i**2)
    return k
A=int(input())
B=int(input())
gen(A,B)
C=iter(gen(A,B))
for i in range(len(A)):
    print(next(C), sep=" ", end=" ")