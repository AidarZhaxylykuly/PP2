thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
#{'cherry', 'apple'}


thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
#{'cherry', 'apple'}


thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)
#Random removing


thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)
#{}


thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)
#Completely deletes the set