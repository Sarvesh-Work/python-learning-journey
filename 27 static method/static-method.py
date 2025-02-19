# *** static method ***

# A static method in Python is a method inside a class that does not depend on the instance (object) or class variables (self)
# It behaves like a normal function but is grouped inside a class for better organization

# note-->
#    It does not access instance (self) 
# Can be called using the class name
# we define  statice method using @staticmethod decorator
 
# example --->
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

# Calling static method using class name (No object needed)
result = MathUtils.add(5, 3)
print(f"Sum: {result}")  # Output: Sum: 8


#  No need to create an object (MathUtils())
# Works like a normal function inside the class

# but  still we can access this method with object

m=MathUtils()
output=m.add(5,3) #-- this will also work
print(output) 


# Static methods are useful in situations where you want a function to be part of a class
#  but it does not need to access or modify instance (self) or class (cls) attributes
#  They help keep the code organized and maintain logical grouping of related functions inside a class