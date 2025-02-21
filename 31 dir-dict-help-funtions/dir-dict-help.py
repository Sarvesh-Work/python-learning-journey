# *** dir dict help functions ***

# 1.dir()
# It shows  a list of all the valid attributes (like variables) and methods (like functions) you can use with an object or class


# ex --->
# example we have a class
class Person:
    def __init__(self, name):
        self.name = name
    
    def say_hello(self):
        print("Hello!")

person = Person("Alice")
print(dir(person)) 
 # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'name', 'say_hello']


# The output shows all the attributes and methods available to the person object
# It includes special attributes like __init__, __str__, and __dict__
# It also includes the name attribute and the say_hello method
# You can use these attributes and methods with the object like this:
print(person.name)  # Alice
person.say_hello()  # Hello!


#2. __dict__ Attribute

# It’s a dictionary that stores the objects instance variables (and sometimes class variables) and their values
# It shows you the data (attributes) an object is holding onto

# ex--->

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 25)
print(person.__dict__)  # {'name': 'Alice', 'age': 25}

# The output shows the instance variables (name and age) and their values
# __dict__ only shows instance-specific stuff (like self.name) not methods or class-level variables (unless they’re explicitly added to the instance)


# 3.help() function

# It shows the documentation (docstring) of a class, method, or function
# It’s useful for understanding what a class or method does, what parameters it takes, and what it returns

# ex--->


# Show documentation for the Person class
print(help(Person))
# in this format
# Help on class Person in module __main__:

# class Person(builtins.object)
#  |  A class to represent a person.
#  |
#  |  Methods defined here:
#  |
#  |  __init__(self, name,age)
#  |
#  |  say_hello(self)
#  |      Say hello to the person.
# ...

