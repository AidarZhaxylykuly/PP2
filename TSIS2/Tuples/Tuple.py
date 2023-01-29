thistuple = ("apple", "banana", "cherry")
print(thistuple)
#('apple', 'banana', 'cherry')


thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
#('apple', 'banana', 'cherry', 'apple', 'cherry')


thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
#3


#Tuple
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
'''
<class 'tuple'>
<class 'str'>
'''


tuple1 = ("apple", "banana", "cherry")#Ok
tuple2 = (1, 5, 7, 9, 3)#Ok
tuple3 = (True, False, False)#Ok
tuple1 = ("abc", 34, True, 40, "male")#Ok


mytuple = ("apple", "banana", "cherry")
print(type(mytuple))
#<class 'tuple'>


thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
#('apple', 'banana', 'cherry')