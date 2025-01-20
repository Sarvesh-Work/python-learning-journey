# a list in python is a collection data type used to store multiple items in a single variable

# Characteristics of Lists:
#  Maintain order of items, starting index at 0
#  Can be modified (add, remove, or change items)
#  Can store different data types (e.g., integers, strings, floats, other lists)
#  Allow duplicate items

my_list = [4, 5, "hi", "hello"]

# print the entire list
print("Full list:", my_list) #-- output =[4, 5, "hi", "hello"]

# access individual value at index 3
print("Value at index 3:", my_list[3])

# list comprehension to create a list of string representations of each item
stringified_list = [str(item) for item in my_list]
print("Stringified list:", stringified_list) # -- output=Stringified list: ['4', '5', 'hi', 'hello']
