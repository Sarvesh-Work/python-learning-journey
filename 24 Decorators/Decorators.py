# Decorators in Python
# A decorator is a function that takes another function as input
# It adds some functionality to the function and returns a modified version
# A decorator allows us to wrap a function and execute additional logic before/after the wrapped function runs
# The @ decorator_name syntax is used to apply the decorator

# ex: A decorator that prints something before and after executing the original function

def decorator_function(fx):  # Takes a function as input
    def fun(*args, **kwargs):  # Allows for any number of arguments
        print("hello")  # Logic before calling the original function
        fx(*args, **kwargs)  # Calls the original function
        print("end")  # Logic after calling the original function
    return fun  # Returns the modified function

@decorator_function  # Applying the decorator to the function
def main_function(a, b):
    print(a + b)

# The decorator adds functionality before and after the actual function execution
# Running the function
main_function(3, 4)  
# Output: 
# hello
# 7
# end


# we can simply add that print("hello")  print("end") in side the main function also 
# it is true instead of defining decorator
# but if we have multiple function and we want to add   print("hello")  print("end") to them so we have to write it inside every function which we can do 
# but it is time taken so for that we can use decorator



# ex with **kwargs to handle keyword arguments

def print_info(**kwargs):  # Accepts any number of keyword arguments
    for key, value in kwargs.items():  # Iterates over the passed keyword arguments
        print(f"{key}: {value}")  # Prints the key and value

# calling the function with keyword arguments
print_info(name="Alice", age=25)  
# output: 
# name: Alice
# age: 25
