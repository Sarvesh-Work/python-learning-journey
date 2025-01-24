# functions in Python are used to encapsulate reusable blocks of code
# this avoids repetitive code, enhances modularity, and simplifies debugging

# Syntax for defining a function------
# def function_name(arguments):
#     # Function body (logic)
#     return value (optional)

# example: a function to perform multiplication of two numbers
def multiplication(a, b):
    """
    This function takes two arguments 'a' and 'b',
    multiplies them, and prints the result.
    """
    result = a * b  # Perform multiplication
    print("Multiplication result:", result)

# Function call:
multiplication(20, 40)  # Output: Multiplication result: 800


# Functions can include:
# 1. Default Arguments
# 2. Keyword Arguments
# 3. Variable-Length Arguments
# 4. Required Arguments


# 1. Default Arguments:
# If a value is not provided for an argument during the function call
# a default value is used

def printData(fname="Alex", lname="Rider"):
    """
    This function prints the full name of a user
    If the user doesn't provide a first or last name it defaults to 'Alex Rider'
    """
    print("Full Name:", fname + " " + lname)

# examples:
printData()  # No arguments provided, so default values are used. Output: Full Name: Alex Rider
printData("Chris", "Martin")  # Output: Full Name: Chris Martin
printData("Chris")  # Only first name provided, last name defaults. Output: Full Name: Chris Rider


# 2. Keyword Arguments:
# These allow you to specify arguments in any order by explicitly naming them

def numbers(a, b):
    """
    This function prints two numbers.
    """
    print("First Number:", a, ", Second Number:", b)

# examples:
numbers(b=90, a=56)  # Arguments are passed in reverse order using keywords. Output: First Number: 56 , Second Number: 90


# 3. Variable-Length Arguments:
# Sometimes, you might want a function to accept an arbitrary number of arguments.

def sum_numbers(*args):
    """
    This function accepts a variable number of arguments
    and print their sum
    """
    total = sum(args)  # 'args' is a tuple containing all arguments
    print("Sum of numbers:", total)

# Examples:
sum_numbers(10, 20, 30)  # Output: Sum of numbers: 60
sum_numbers(5, 15)  # Output: Sum of numbers: 20


# 4. Required Arguments:
# These are mandatory arguments that must be provided when the function is called.
# If omitted, Python will raise a TypeError.

def divide(a, b):
    """
    This function divides two numbers
    Both 'a' and 'b' must be provided as arguments
    """
    if b != 0:  # Prevent division by zero
        return a / b  # Return the result of division
    else:
        return "Division by zero is not allowed"

# Examples:
result = divide(20, 5)  # Output: 4.0
print("Division result:", result)
print("Division result:", divide(20, 0))  # Output: Division by zero is not allowed


# **The Return Keyword**
# The return statement is used to send the result of a function's computation
# back to the caller Unlike print which only displays the result
# return allows the result to be reused elsewhere in the code.

def square(num):
    """
    This function calculates the square of a number
    and returns the result.
    """
    return num * num  # The result is sent back to the caller

# Examples:
result = square(5)  # The returned value is stored in 'result'
print("Square:", result)  # Output: Square: 25
