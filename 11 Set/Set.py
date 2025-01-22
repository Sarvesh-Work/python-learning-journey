# *** set ***

# A set is an unordered collection of items
# Every element is unique (no duplicates) and must be immutable (which cannot be changed)
#  Sets are written with curly brackets {}
#  Sets are mutable, meaning you can add or remove elements
# set dose not support indexing 

s={1,2,3,4,5,2}
# now in this we have duplicate value 2 but when we print the set it will remove the duplicates and print the unique values
# means it will not consider the repeated values
print(s) # output={1, 2, 3, 4, 5  -- there is no guarantee that the order will be the same as the order in which the elements were added to the set 


# we can also create set using set() constructor
s1=set({1,2,3,4,5,2}) 
print(s1) # output={1, 2, 3, 4, 5}  -- there is no guarantee that the order will be the same as the order in which the elements were added to the set 

# we can not create empty set using {} because it will create an empty dictionary
# to create an empty set we have to use set() constructor

s2=set()
print(s2) # output=set() -- this will create an empty set




