l=input()
k=0
for i in range(len(l)):
    if l[i]==3:
        k+=1
    else:
        k=0
    if k==2:
        print('True')
        quit()