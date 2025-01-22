# *** tuples methods ***


# 1. count()
# this method returns the number of times a specified value appears in the tuple

tuple1 = ("hi", "hi", "hi", 5, "hello", 7, 8, 2, 1)
value_to_count = "hi"
count_of_value = tuple1.count(value_to_count)
print(f"The value '{value_to_count}' appears {count_of_value} time in the tuple.") # output=3

# 2. index()
# this method returns the index of the first occurrence of a specified value in the tuple
# if the value is not in the tuple, it raises a ValueError

tuple2 = ("hi", 3, 4, 5, "hello", 7, 8, 2, 1)
value_to_find = 5
index_of_value = tuple2.index(value_to_find)
print(f"The index of the value '{value_to_find}' is {index_of_value} in the tuple.") # output=3

# index with start and end parameters
index_of_value = tuple2.index(value_to_find, 4, 7)
print(f"The index of the value '{value_to_find}' is {index_of_value} in the tuple.") # error

# 3. len()
# this method returns the number of elements in the tuple

tuple3 = ("hi", 3, 4, 5, "hello", 7, 8, 2, 1)
length_of_tuple = len(tuple3)
print(f"The length of the tuple is {length_of_tuple}.") # output=9

# 4. max() -- only used for numbers
# this method returns the maximum value in the tuple
list1 = (3, 6, 1, 5, 4, 8, 7)
max_value = max(list1)
print(f"The maximum value in the tuple is {max_value}.") # output=8

# 5. min() -- only used for numbers
# this method returns the minimum value in the tuple
list2 = (3, 6, 1, 5, 4, 8, 7)
min_value = min(list2)  
print(f"The minimum value in the tuple is {min_value}.") # output=1 

# 6. sum() -- only used for numbers
# this method returns the sum of all the elements in the tuple
list3 = (3, 6, 1, 5, 4, 8, 7)
sum_of_elements = sum(list3)
print(f"The sum of all elements in the tuple is {sum_of_elements}.") # output=34

# 7. sorted()
# this method returns a new sorted list from the elements of the tuple
# the original tuple remains unchanged
list4 = (3, 6, 1, 5, 4, 8, 7)
sorted_list = sorted(list4)
print(f"The sorted list is {sorted_list}.") # output=[1, 3, 4, 5, 6, 7, 8]

# 8. any()
# this method returns True if any element in the tuple is True
# otherwise, it returns False
tuple4 = (True, False, False)
result = any(tuple4)
print(f"The result of the 'any' method is {result}.") # output=True

# 9. all()
# this method returns True if all elements in the tuple are True
# otherwise, it returns False
tuple5 = (True, True, True)
result = all(tuple5)
print(f"The result of the 'all' method is {result}.") # output=True


# 10. tuple()
# this method creates a new tuple from an iterable object   
list5 = [3, 6, 1, 5, 4, 8, 7]
new_tuple = tuple(list5)
print(f"The new tuple is {new_tuple}.") # output=(3, 6, 1, 5, 4, 8, 7)

# 11. reversed()
# this method returns a reverse iterator over the values of the tuple
# the original tuple remains unchanged
tuple6 = (3, 6, 1, 5, 4, 8, 7)
reversed_tuple = reversed(tuple6)
print(f"The reversed tuple is {tuple(reversed_tuple)}.") # output=(7, 8, 4, 5, 1, 6, 3)

# 12. zip()
# this method returns a zip object that combines elements from two or more tuples
# the resulting zip object can be converted to a list, tuple, or dictionary
tuple7 = (3, 6, 1, 5, 4, 8, 7)
tuple8 = (2, 4, 6, 8, 10, 12, 14)
zipped_tuple = zip(tuple7, tuple8)
print(f"The zipped tuple is {tuple(zipped_tuple)}.") # output=((3, 2), (6, 4), (1, 6), (5, 8), (4, 10), (8, 12), (7, 14))

