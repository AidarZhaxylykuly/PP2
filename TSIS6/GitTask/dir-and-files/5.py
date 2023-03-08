f=open('5file.txt', 'a')
l = [a for a in input().split()]
for i in l:
    f.write(i)
    f.write('\n')
f.close()