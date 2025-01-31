# Local and Global Variables

# Local variables are declared inside a function or block and can only be accessed within that scope
def local_example():
    x = 78  # Local variable
    print(x)  # Output: 78

local_example()
# print(x)  # Uncommenting this will raise an error since 'x' is not accessible outside the function

# Global variables are declared outside functions and can be accessed anywhere in the program
y = 56  # Global variable

def global_example():
    print(y)  # Output: 56

global_example()

# Local and Global Variable Conflict
z = 80  # Global variable

def local_global_conflict():
    z = 87  # Local variable with the same name as the global variable
    print(z)  # Output: 87 (Local variable takes precedence over global variable)

local_global_conflict()
print(z)  # Output: 80 (Global variable remains unchanged)

# Accessing a Global Variable Inside a Function Using 'global' Keyword
p = 90  # Global variable

def modify_global():
    global p  # Declaring 'p' as a global variable
    p = 67  # Modifying the global variable
    print(p)  # Output: 67

modify_global()
print(p)  # Output: 67 (Global variable is now updated)