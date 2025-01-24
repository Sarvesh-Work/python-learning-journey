# *** if-else in Python ***

# The `if-else` statement is used to make decisions based on a condition
# - If the condition evaluates to `True` the code inside the `if` block is executed
# - if the condition evaluates to `False`the code inside the `else` block is executed

# Conditional operators used in conditions include:
# >, <, >=, <=, ==, != (greater than, less than, greater than or equal to)

# Example:

# let's say ihave 4 apples, and i want to set the price based on their count----
# - If the number of apples is less than 4 the price should be 5.
# - If the number of apples is 4 or more, the price should be 80

apple = 4  # Number of apples

# using if-else to decide the price----
if apple < 4:
    print(50)  # Prints 50 if the number of apples is less than 4
else:
    print(80)  # Prints 80 if the number of apples is 4 or more

# here  apple = 4, the condition apple < 4 is False, so the else block is executed printing 80