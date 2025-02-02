# *** Lambda Functions in Python ***

# Lambda functions are anonymous (nameless) functions that are useful for writing small, one-line functions
# They provide a concise way to define simple functions without using the `def` keyword

# Example: Normal function for addition
def add(x, y):
    print(x + y)  # Prints the sum of x and y

add(4, 5)  # Output: 9


# Optimized version using a Lambda Function


# lambda function for additions
add = lambda x, y: print(x + y)  # This is a shorthand function

add(7, 8)  # Output: 15


# key Differences Between Normal and Lambda Functions

# 1. **Normal Function:**
#    - Uses the `def` keyword
#    - Can contain multiple statements
#    - More readable for complex logic

# 2. **Lambda Function:**
#    - Defined using the `lambda` keyword
#    - Can only contain a single expression
#    - Best for short, one-line operations


# ----------------------------------
# NOTE: 
# Lambda functions are **only recommended** for short and simple functions
# For more complex logic, use normal functions with `def` for better readability and maintainability
