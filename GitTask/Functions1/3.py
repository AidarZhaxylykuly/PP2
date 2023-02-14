def solve(h, l):
    for i in range(h+1):
        if i*4+(35-i)*2==l:
            print(f"{i} rabbits and {35-i} chickens")

h=35
l=94
solve(h, l)