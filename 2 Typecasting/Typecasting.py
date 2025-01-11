# --- Typecasting in Python ---

# Typecasting refers to converting one data type to another.
# There are two types of typecasting:
# 1. Explicit Typecasting (Manual)
# 2. Implicit Typecasting (Automatic)

# 1. Explicit Typecasting
# Explicit typecasting requires us to manually convert one data type to another using built-in functions like int(), str(), float(), etc.
# developer explicitly converts one data type in to another data type using those functions
a = 1
b = 2

# Adding two integers
print(a + b)  # Output: 3

# Explicit typecasting: Converting integers to strings and concatenating them
print(str(a) + str(b))  # Output: '12' (1 and 2 are combined as strings)

# 2. Implicit Typecasting
# Implicit typecasting happens automatically when Python converts a smaller data type to a larger one.
# Example: Converting int to float automatically when performing arithmetic operations.

x = 5       # int
y = 2.5     # float

# Implicit typecasting: Adding int and float automatically converts int to float
result = x + y
print(result)  # Output: 7.5 (int x is automatically converted to float)

# Type of the result
print(type(result))  # Output: <class 'float'>
