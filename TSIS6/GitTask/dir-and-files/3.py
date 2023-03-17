import os
p=input('Write the directory: ')
print("A path exists:", os.path.exists(p))


if os.path.exists(p):
    print(os.path.basename(p))
    print(os.path.dirname(p))