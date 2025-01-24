# --- Input Function in Python ---

# The input() function is used to take user input in Python.
# By default, the input is always stored as a string, so if we need a specific data type (e.g., int, float), we must explicitly typecast it.

# Example: Taking a user's name as input (string type)
name = input("Enter your name: ")
print("Hello:",name)  # Output: Hello, [name]

# Example: Taking an integer input and typecasting it to an integer using int()
number1 = int(input("Enter number1: "))  # Typecasting string input to int
print("Type of number1:",type(number1))  # Output: <class 'int'>

# Example: Taking a float input and typecasting it to float using float()
number2 = float(input("Enter number2: "))  # Typecasting string input to float
print("Type of number2:",type(number2))  # Output: <class 'float'>
