def un(A):
    B=[]
    for i in range(len(A)):
        if A[i] in B:
            continue
        else:
            B.append(A[i])
    print(B)
A=input()
un(A)