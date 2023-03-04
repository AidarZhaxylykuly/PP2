def spy_game(A):
    for i in range(len(A)):
        if A[i]!='0' and A[i]!='7':
            A=A[:i]+'H'+A[i+1:]
    A=A.replace('H', '')
    if A!='007':
        print(A)
        print(False)
        quit()
    print(True)
l=input()
A=''
for i in range(len(l)):
    A+=str(l[i])
spy_game(A)