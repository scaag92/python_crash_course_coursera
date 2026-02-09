"""
SETS

Is a built-in data type it is used to store a collection of items, based on the mathematical concept sets:

1 - Unordered = The items don't have order. They may appear in a different order every time that we see it.
2 - Unique = Every element must be unique. Duplicated values are automatically removed
3 - Mutable Element = Sets are mutable, we could add or remove without any problem, but the items itself must be inmutable.

"""
#---------------------------------------------------------------------------------------------------------------------------------------------------

""" 

Creating a Set:

"""
set1 = {"1","2","3","4","5"}
print (set1)

list_1 = [10,12,13,14,15,16,17]
set2 = set(list_1)
print (set2)

# CREATING AN EMPTY SET

empty_set = set()

#---------------------------------------------------------------------------------------------------------------------------------------------------

""" 

Adding and removing Elements:

Add a single item
add(item)

Add multiple elements from a list or another set
update([item1, item2])

Removes an item, raises an error if the item is not found
remove(item)

This method will remove the item but don't raise an error if the item is not found
discard(item) 

This method will return a random element 
pop() 
"""

#ADD
set1.add(6)
print("ADD")
print(set1)

#UPDATE
list_2 = [7,8]
set1.update(list_2)
print("UPDATE")
print(set1)

#REMOVE
set1.remove(6)
print("REMOVE")
print(set1)

#DISCARD
set1.discard(8)
print("DISCARD")
print(set1)

#POP
print("DISCARD")
print(set1.pop())

#---------------------------------------------------------------------------------------------------------------------------------------------------

""" 

Mathematical Set Operations
Because set are unordered, we cannot access item by index, instead we use these methods

UNION  |
All elements from both sets

INTERSECTION &
Only elements that are present in both sets

DIFFERENCE -
The elements from A that aren't in SET B

SYMETRIC DIFFERENCE ^
The elements in either set but NOT both

"""

set3 = {"1","2","3","4","5"}
print (set3)


set4 = {"2","4","6","8","9"}
print (set4)

# UNION
print("SET UNION")
print(set3 | set4)

#INTERSECTION
print("SET INTERSECTION")
print(set3 & set4)

#DIFFERENCE
print("SET DIFFERENCE")
print(set3 - set4)

#SYMMETRIC DIFFERENCE
print("SET SYMMETRIC DIFFERENCE")
print(set3 ^ set4)



