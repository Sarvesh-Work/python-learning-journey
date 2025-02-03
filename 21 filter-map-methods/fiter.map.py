# *** filter map ***

# map
# map= The map() function in Python is used to apply a given function to each item of an iterable (such as a list, tuple, etc.) 
# and return a map object (which is an iterator). 
# The map() function is often used when you want to perform an operation on each element of an iterable without writing an explicit loop.


# Function to add two numbers
def add(x, y):
    # The function takes two arguments x and y, and returns their sum
    return x + y

# two lists of numbers (iterables)
number1 = [2, 3, 4, 5, 6]  # First list of numbers
number2 = [6, 7, 3, 4, 2]  # Second list of numbers

# use map to apply the 'add' function to corresponding elements of both lists
# map() applies the function to each pair of elements from number1 and number2
addition = list(map(add, number1, number2))  # Convert map object to a list

# Print the result of adding corresponding elements
print(addition)  # Output: [8, 10, 7, 9, 8]



# using lambda to add two numbers
addition_lambda = list(map(lambda x, y: x + y, number1, number2))

# Print the results
print(addition_lambda)  # Output: [8, 10, 7, 9, 8]


# filter 
# the filter() function in Python is used to filter elements from an iterable based on a given condition
# It applies a function to eachs item in the iterable and returns an iterator containing only those items for which the function returns true

# now lets create a function
# which returns the number which are divided by 2

def is_divisible_by_two(num):
    # check if the number is divisible by 2 (even number)
    if (num % 2 == 0):
        return num  # return the number if it's divisible by 2

# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# using filter to apply the is_divisible_by_two function to the numbers list
# filter() will include only those numbers that are divisible by 2 (i.e., even numbers)
even_numbers = filter(is_divisible_by_two, numbers)

# Convert the filter object to a list and print the result
# The result is an iterator, so we need to convert it to a list to see the output
print(list(even_numbers))  # Output: [2, 4, 6, 8]

# reduce

# the reduce() function in Python is used to apply a function cumulatively to the items in an iterable (like a list or tuple)
# reducing the iterable to a single value
# It processes the iterable from left to rightapplying the function to pairs of elements and keeps accumulating the result

from functools import reduce # --- we have to import the reduce function for us it is not like map pr reduce

# Function to add two numbers
def add(x, y):
    return x + y

# List of numbers
numbers = [1, 2, 3, 4]

# Using reduce to sum up all the numbers in the list
total = reduce(add, numbers)

# Output the result
print(total)  # Output: 10 (1 + 2 + 3 + 4)
