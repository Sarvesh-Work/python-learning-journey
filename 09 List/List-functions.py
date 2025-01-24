# *** List methods ***

# 1. append()
# this method is used to add a new value at the end of the list
# Note: It adds only one value at a time

my_list = [1, 3, 5, "hi"]
my_list.append(3)
print("After append:", my_list)

# 2. sort()
# This method is used to sort the list
# It sorts the list in increasing order by default
# Use `reverse=True` to sort in decreasing order

# Sorting a list of numbers
numbers = [3, 6, 1, 5, 4, 8, 7]
numbers.sort()  # Increasing order
print("Sorted in increasing order:", numbers)

numbers.sort(reverse=True)  # Decreasing order
print("Sorted in decreasing order:", numbers)

#  we can't  use sort with mixed data types
# The sort() method requires all elements in the list to be comparable with each other.
# For example, python cannot compare a string ("hi") with an integer (3) because they are different data types.
# Attempting to sort a list with mixed data types will raise a typeError

# example of incompatible list for sorting:
# mixed_list = [3, "hi", 5]
# mixed_list.sort()  # This will raise a TypeError


# 3. reverse()
# this method reverses the order of elements in the list

numbers2 = [3, 6, 1, 5, 4, 8, 7]
numbers2.reverse()
print("Reversed list:", numbers2)

# 4.index()
# this method returns the index of the first occurrence of a specified value in the list
# if the value is not in the list, it raises a ValueError
numbers3= [3, 6, 1, 5, 4, 8, 7]

# we have to find the index of 5 in list
print(numbers3.index(5)) # output=3


# 5. count()
# this method is used to count how many times a specific value appears in a list

fruits = ["apple", "apple", "banana", "orange", "mango", "papaya"]

# Value to count occurrences of
value_to_count = "apple"
count_of_value = fruits.count(value_to_count)

# print the result with context
print(f"The value '{value_to_count}' appears {count_of_value} time(s) in the list.")

# 6. copy()
# this method creates a shallow copy of the list

original_list = [3, 4, 5, 6, 7, 8]
copied_list = original_list.copy()
print("Copied list:", copied_list)

# 7. insert()
# this method inserts a given value at a specified index.

list_to_modify = [3, 4, 5, 6, 7, 8]
index_to_insert = 3
value_to_insert = 45

# Insert the value at the specified index
list_to_modify.insert(index_to_insert, value_to_insert)
print(f"List after inserting {value_to_insert} at index {index_to_insert}:", list_to_modify)

# 8. extend()
# this method extends the list by adding elements from another iterable

list_a = [1, 2, 3, 4]
list_b = [60, 70, 80]

# Extend list_b by adding elements from list_a
list_b.extend(list_a)
print(f"List B after extending with List A: {list_b}")

# 9. remove()
# this method removes the first occurrence of a specified value from the list
# if the value is not in the list, it raises a ValueError
list_to_remove_from = [3, 4, 5, 6, 7, 8]
value_to_remove = 5
list_to_remove_from.remove(value_to_remove)
print(f"the {value_to_remove} is removed from the list: {list_to_remove_from}")

# 10. pop()
# this method removes the element at the specified index and returns it
# if no index is specified, it removes and returns the last element in the list
list_to_pop = [3, 4, 5, 6, 7, 8]
# remove the element at index 3
popped_element = list_to_pop.pop(3)
print(f"List after popping element at index 3: {list_to_pop}") # output=[3, 4, 5, 7, 8]
popped_element_without_index = list_to_pop.pop()  # remove the last element if no index is specified
print(f"List after popping the last element: {list_to_pop}") # output=[3, 4, 5, 7]

# 11. clear()
# this method removes all elements from the list
list_to_clear = [3, 4, 5, 6, 7, 8]
list_to_clear.clear()
print(f"List after clearing all elements: {list_to_clear}") # output=[]



