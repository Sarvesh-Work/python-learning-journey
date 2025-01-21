# *** f string ***


# the f-string is a way to format strings in Python. It is a string prefixed with 'f' or 'F' and can contain expressions inside curly braces {}. 
# The expressions are evaluated at runtime and then formatted using the format() protocol
# this format is available in Python 3.6 and later versions.

# example:
name = "Alice"
age = 25
print(f"Hello, my name is {name} and I am {age} years old.") # output=Hello, my name is Alice and I am 25 years old

# f-strings can also be used for calculations
num1 = 10
num2 = 20
print(f"The sum of {num1} and {num2} is {num1 + num2}.") # output=The sum of 10 and 20 is 30.

# f-strings can also be used to call functions
def greet():
    return "Hello, World!"

print(f"{greet()}") # output=Hello, World!

# f-strings can be used to format numbers
pi = 3.14159
print(f"The value of pi is {pi:.2f}.") # output=The value of pi is 3.14.
# that :.2f is used to format the number to 2 decimal places.

# f-strings can be used to format dates
from datetime import datetime

today = datetime.today()
print(f"Today's date is {today:%B %d, %Y}.") 


