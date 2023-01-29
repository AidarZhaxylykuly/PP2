thislist = ["apple", "banana", "cherry"]
print(thislist)
#['apple', 'banana', 'cherry']


thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
#['apple', 'banana', 'cherry', 'apple', 'cherry']


thislist = ["apple", "banana", "cherry"]
print(len(thislist))
#3


list1 = ["apple", "banana", "cherry"]#Ok
list2 = [1, 5, 7, 9, 3]#Ok
list3 = [True, False, False]#Also Ok


list1 = ["abc", 34, True, 40, "male"]#Still ok


mylist = ["apple", "banana", "cherry"]
print(type(mylist))
#<class 'list'>


thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
#['apple', 'banana', 'cherry']


