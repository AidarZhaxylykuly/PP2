def pal(s):
    if s==s[::-1]:
        print(True)
    else:
        print(False)
s=input()
pal(s)