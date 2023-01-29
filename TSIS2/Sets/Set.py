thisset = {"apple", "banana", "cherry"}
print(thisset)
#{'cherry', 'apple', 'banana'}
# Set list is unordered, meaning: the items will appear in a random order.


thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
#{'cherry', 'apple', 'banana'}


thisset = {"apple", "banana", "cherry"}
print(len(thisset))
#3


set1 = {"apple", "banana", "cherry"}#Ok
set2 = {1, 5, 7, 9, 3}#Ok
set3 = {True, False, False}#Ok
set1 = {"abc", 34, True, 40, "male"}#Ok


myset = {"apple", "banana", "cherry"}
print(type(myset))
#<class 'set'>


thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
#{'cherry', 'apple', 'banana'}