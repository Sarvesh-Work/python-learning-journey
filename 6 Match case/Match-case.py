# *** match case ***

# The match-case statement was introduced in Python 3.10 and allows you to match a variable or value against different conditions in a more readable way than traditional if-elif-else statements.
# The match keyword starts the pattern matching process.
# The case keyword is used to define the conditions you want to check.

# ex-----

# ask the user to input a number
number = int(input("Enter the number: "))  # convert the input to an integer typecasting
# using input function for user input

# use match-case to check for different values of 'number'
match number:
    case 0:
        # If the number is 0, print a message
        print("Number is zero")
    case 4:
        # If the number is 4, print a message
        print("Number is 4")
    case 5:
        # If the number is 5, print a message
        print("Number is 5")
    case _: # you can consider this as default case
        # The _ case acts as a default. It will match anything not caught by previous cases.
        print("Number is not 0, 4, or 5")  # This case will catch all other numbers
     

