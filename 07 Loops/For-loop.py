# *** for Loop ***

# A for loop is used to iterate over a sequence such as a string, list or range of numbers.

# Example 1: Iterating over a string
name = "alex"
# To print each character of the word " alex we can use a for loop.
for character in name:
    print(character)

# Output:
# a
# l
# e
# x

# Example 2: Using the range() function
# The range() function is used to generate a sequence of numbers
# making it useful for performing tasks multiple times

# To print numbers from 0 to 9:
for k in range(10):  # range(10) generates numbers from 0 to 9.
    print(k)

# Output:
# 0
# 1
# 2
# ...
# 9

# The range() function can also take a starting point, an ending point 
#  an optional step value to customize the sequence

# Example 3: Specifying a start and end range
# To print numbers from 1 to 10:
for k in range(1, 11):  # range(start, stop) stops at stop-1
    print(k)

# Output:
# 1
# 2
# ...
# 10

# Example 4: Using a step value
# to print only even numbers from 2 to 10:
for k in range(2, 11, 2):  # range(start, stop, step)
    print(k,"new")

# Output:
# 2
# 4
# 6
# 8
# 10

# The step value in a range() function determines the increment (or decrement) between each number in the generated sequence. It specifies how much the current value should increase or decrease with each iteration.
