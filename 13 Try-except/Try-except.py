# *** try-except for error handling ***

# try and except is use to handle errors in python
# If you don't use try-except, the program will stop executing and show an error message
# But if you use try-except, the program will continue executing and show a message that you want to show when an error occurs


# ex: Handling division by zero error
try:
    num1 = 10
    num2 = 0
    print(num1 / num2)
except ZeroDivisionError:
    print("Cannot divide by zero")

print("Program continues executing")

# if i dont use try-except, the program will stop executing and show an error message
# and that "Program continues executing" will not be printed beacuse the program has stopped executing

# but if i use try-except, the program will continue executing and show a message that i want to show when an error occurs
# we can handle multiple errors in a single try-except block

# one more thing, we can use else and finally block with try-except
# else block will execute when there is no error


# finally block will execute no matter what
# it will execute whether there is an error or not
# it is used to clean up resources like closing a file or a database connection
# it is used to run code that should always run even if there is an error

# usinf finally block

try:
    num1 = 10
    num2 = 0
    print(num1 / num2)
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("This will always run")



