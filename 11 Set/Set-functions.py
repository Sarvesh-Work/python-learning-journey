# *** set functions ***

# 1. add()
# this method adds an element to the set
# if the element is already present in the set, the set remains unchanged
s = {1, 2, 3, 4, 5}
s.add(6)
print(f"The updated set is {s}.") # output={1, 2, 3, 4, 5, 6}

# 2. remove()
# this method removes the specified element from the set
# if the element is not present in the set, it raises a KeyError
s1 = {1, 2, 3, 4, 5}
s1.remove(3)
print(f"The updated set is {s1}.") # output={1, 2, 4, 5}

# 3. union()
# this method returns a new set containing all the elements from the original set and another set
# it performs the union operation on the sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
union_set = set1.union(set2)
print(f"The union of set1 and set2 is {union_set}.") # output={1, 2, 3, 4, 5, 6, 7, 8}
# set1 and set2 will remain unchanged
# union will return the new set


# 4. update()
# this method updates the set with the union of itself and another set
# it performs the union operation on the sets and updates the original set
set3 = {1, 2, 3, 4, 5}
set4 = {4, 5, 6, 7, 8}
set3.update(set4)
print(f"The updated set3 is {set3}.") # output={1, 2, 3, 4, 5, 6, 7, 8}

# in this the set3 will be updated with the union of set3 and set4
# unlike union method it will not return a new set it will update the original set

# 5. intersection()
# this method returns a new set containing the common elements from the original set and another set
# it performs the intersection operation on the sets
set5 = {1, 2, 3, 4, 5}
set6 = {4, 5, 6, 7, 8}
intersection_set = set5.intersection(set6)
print(f"The intersection of set5 and set6 is {intersection_set}.") # output={4, 5}
# set5 and set6 will remain unchanged
# intersection will return the new set

# 6. intersection_update()
# this method updates the set with the intersection of itself and another set
# it performs the intersection operation on the sets and updates the original set
set7 = {1, 2, 3, 4, 5}
set8 = {4, 5, 6, 7, 8}
set7.intersection_update(set8)
print(f"The updated set7 is {set7}.") # output={4, 5}
# in this the set7 will be updated with the intersection of set7 and set8
# unlike intersection method it will not return a new set it will update the original set

# 7. difference()
# this method returns a new set containing the elements from the original set that are not in another set
# it performs the difference operation on the sets
set9 = {1, 2, 3, 4, 5}
set10 = {4, 5, 6, 7, 8}
difference_set = set9.difference(set10)
print(f"The difference between set9 and set10 is {difference_set}.") # output={1, 2, 3}
# set9 and set10 will remain unchanged
# difference will return the new set

# 8. difference_update()
# this method updates the set with the difference of itself and another set

set11 = {1, 2, 3, 4, 5}
set12 = {4, 5, 6, 7, 8}
set11.difference_update(set12)
print(f"The updated set11 is {set11}.") # output={1, 2, 3}
# in this the set11 will be updated with the difference of set11 and set12

# 9. symmetric_difference()
# this method returns a new set containing the elements that are in either of the sets, but not both
# it performs the symmetric difference operation on the sets
set13 = {1, 2, 3, 4, 5}
set14 = {4, 5, 6, 7, 8}
symmetric_difference_set = set13.symmetric_difference(set14)
print(f"The symmetric difference between set13 and set14 is {symmetric_difference_set}.") # output={1, 2, 3, 6, 7, 8}

# 10. symmetric_difference_update()
# this method updates the set with the symmetric difference of itself and another set
set15 = {1, 2, 3, 4, 5}
set16 = {4, 5, 6, 7, 8}
set15.symmetric_difference_update(set16)
print(f"The updated set15 is {set15}.") # output={1, 2, 3, 6, 7, 8}


# 11. isdisjoint()
# this method returns True if two sets have a null intersection
# otherwise, it returns False
set17 = {1, 2, 3, 4, 5}
set18 = {6, 7, 8}
result = set17.isdisjoint(set18)
print(f"Are set17 and set18 disjoint? {result}.") # output=True

# 12. issubset()
# this method returns True if all elements of a set are present in another set
# otherwise, it returns False
set19 = {1, 2, 3}
set20 = {1, 2, 3, 4, 5}
result = set19.issubset(set20)
print(f"Is set19 a subset of set20? {result}.") # output=True

print(set20.issuperset(set19)) # output=True    

# 13. issuperset()
# this method returns True if a set contains all elements of another set
# otherwise, it returns False
set21 = {1, 2, 3, 4, 5}
set22 = {1, 2, 3}
result = set21.issuperset(set22)
print(f"Is set21 a superset of set22? {result}.") # output=True

# 14. pop()
# this method removes and returns an arbitrary element from the set
# if the set is empty, it raises a KeyError
set23 = {1, 2, 3, 4, 5}
popped_element = set23.pop()
print(f"The popped element is {popped_element}.")#  -- the output is not fixed
print(f"The updated set23 is {set23}.") # output={2, 3, 4, 5}
# list pop method and set pop method are different
# list pop method removes the element at the specified index
# set pop method removes an arbitrary element from the set

# 15. clear()
# this method removes all elements from the set
set24 = {1, 2, 3, 4, 5}
set24.clear()
print(f"The set after clearing all elements is {set24}.") # output=set()

# 16. copy()
# this method creates a shallow copy of the set
set25 = {1, 2, 3, 4, 5}
copied_set = set25.copy()
print(f"The copied set is {copied_set}.") # output={1, 2, 3, 4, 5}

# 17. discard()
# this method removes the specified element from the set
# if the element is not present in the set, it does nothing
set26 = {1, 2, 3, 4, 5}
set26.discard(3)
print(f"The updated set26 is {set26}.") # output={1, 2, 4, 5}


#18
