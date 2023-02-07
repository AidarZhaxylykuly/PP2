s=input()
print(s[2], s[-2], s[::5], s[:-2], s[::2], s[1::2], s[::-1], s[::-2], len(s), sep='\n')


s=input()
print(s.count(' ')+1)


s=input()
if len(s)%2==0:
    print(s[len(s)/2:]+s[:len(s)/2])
else:
    print(s[len(s)/2:]+s[len(s)/2+1]+s[:len(s)/2])


s=input()
i=s.find(' ')
print(s[i+1:]+' '+s[:i+1])


s=input()
A=s.find('f')
if A>=0:
    print(A, ' ', end='')
s=s[:A]+'1'+s[A+1:]
A=s.rfind('f')
if A>=0:
    print(A)


s=input()
A=s.find('f')
if A>=0:
    s=s[:A]+'1'+s[A+1:]
    A=s.find('f')
    if A>=0:
        print(A)
    else:
        print('-1')
else:
    print('-2')


s=input()
A=s.find('h')
B=s.rfind('h')
print(s[:A]+s[B+1:])


s=input()
A=s.find('h')
B=s.rfind('h')
print(s[:A]+s[B:A:-1]+s[B+1:])


s=input()
s=s.replace("1", "one")
print(s)


s=input()
s=s.replace("@", "")
print(s)


s=input()
s=s.replace("h", "H")
A=s.find('H')
B=s.rfind('H')
print(s[:A]+'h'+s[A+1:B]+'h'+s[B+1:])


s=input()
a=''
for i in range(len(s)):
    if i%3!=0:
        a+=s[i]
print(a)