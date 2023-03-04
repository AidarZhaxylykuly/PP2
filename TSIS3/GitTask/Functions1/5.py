from itertools import permutations

l=input()
l=l.split(" ")
p=permutations(l)

for i in list(p):
    print(i)