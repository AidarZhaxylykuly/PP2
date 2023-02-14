def filter_prime(l):
    k=0
    for i in range(len(l)):
        for j in range(2, int(l[i])):
            if int(l[i])%j==0:
                k=1
        if k==1:
            k=0
            continue
        print(l[i])
            
l=str(input())
l=l.split(' ')
filter_prime(l)