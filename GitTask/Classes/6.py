def P(n):
    return list(filter(lambda x: all(x%i!=0 for i in range(2,x)) and x>= 2, n))
n=input()
print(P(n))