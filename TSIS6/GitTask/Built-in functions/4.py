from time import sleep
x=int(input())
y=int(input())
z=x**(0.5)
sleep(y/1000)
print('Square root of {} after {} miliseconds is {}'.format(x, y, z))