# *** Tuples ***

# A tuple is a collection of values that is:
#  Tuples maintain the order of elements
#  You cannot modify, add, or remove elements after the tuple is created.
#  A tuple is written within parentheses ()
#  Tuples can store multiple types of data (e.g., integers, strings)
#  While tuples allow duplicates, they don't need to be unique by default like sets

# Example of creating a tuple
tuple1 = ("hi", 3, 4, 5, "hello", 7, 8, 2, 1)

# Print the tuple
print("Original Tuple:", tuple1)

# tuples are immutable, so trying to modify an element results in an error

tuple1[6] = 40  # trying to change an element in the tuple (this will raise an error)


# You can perform slicing on tuples to extract parts of them.
# For example, slicing from index 3 to 6 (exclusive of index 6)
sliced_tuple = tuple1[3:6]
print("Sliced Tuple (index 3 to 6):", sliced_tuple)

