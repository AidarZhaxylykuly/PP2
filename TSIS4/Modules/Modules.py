import mymodule
mymodule.greeting("Jonathan")
a = mymodule.person1["age"]
print(a)



import mymodule as mx
a = mx.person1["age"]
print(a)
#Ok



import platform
x = platform.system()
print(x)
x = dir(platform)
print(x)



x=dir(mymodule)
print(x)



from mymodule import person1
print (person1["age"])