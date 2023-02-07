i = 1
for color in 'red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'violet':
    print('#', i, ' color of rainbow is ', color, sep = '')
    i += 1
##1 color of rainbow is red
##2 color of rainbow is orange
##3 color of rainbow is yellow
##4 color of rainbow is green
##5 color of rainbow is cyan
##6 color of rainbow is blue
##7 color of rainbow is violet


for i in 1, 2, 3, 'one', 'two', 'three':
    print(i)
'''
1
2
3
one
two
three
'''


for i in range(4):  # равносильно инструкции for i in 0, 1, 2, 3:
    # здесь можно выполнять циклические действия
    print(i)
    print(i ** 2)
# цикл закончился, поскольку закончился блок с отступом
print('Конец цикла')
0
#0
#1
#1
#2
#4
#3
#9
#Конец цикла


sum = 0
n = 5
for i in range(1, n + 1):
    sum += i
print(sum)
#15


print(1, 2, 3)
print(4, 5, 6)
print(1, 2, 3, sep=', ', end='. ')
print(4, 5, 6, sep=', ', end='. ')
print()
print(1, 2, 3, sep='', end=' -- ')
print(4, 5, 6, sep=' * ', end='.')
'''
1 2 3
4 5 6
1, 2, 3. 4, 5, 6. 
123 -- 4 * 5 * 6.
'''