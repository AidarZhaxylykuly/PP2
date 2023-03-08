A='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in A:
    f=open('{}.txt'.format(i), 'a')
    f.close()