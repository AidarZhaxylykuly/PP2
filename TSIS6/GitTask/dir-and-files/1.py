import os
print(os.getcwd())
p=input('Write the directory: ')
for i in os.listdir(p):
    if os.path.isdir(os.path.join(p, i)):
        print(i)


print(os.listdir(p))