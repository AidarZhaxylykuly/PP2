s=input()
if s==s[::-1]:
    print('Ok')
else:
    print('Not ok')
    print(reversed(s))