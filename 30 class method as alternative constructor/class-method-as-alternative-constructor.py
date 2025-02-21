# *** class method as alternative constructor ***

# Normally we  create an object from a class using the __init__ method which is the default constructor
#  It sets up the object with the values you pass when you make a new instance

# like this -->
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Normal way to create an object
person = Person("Alice", 25)


# now consider if a data comes in different format (e.g., a string or a dictionary)and you need to process it first
# This is where a class method comes in handy
# To make a class method we use the @classmethod decorator
# in this the  first parameter is usually called cls (instead of self), which refers to the class


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def from_string(cls, data_string):
        # Example: data_string = "Alice-25"
        name, age = data_string.split("-")
        return cls(name, int(age))  # Creates a new Person object

# Using the class method as an alternative constructor
person = Person.from_string("Alice-25")
print(person.name)  # Output: Alice
print(person.age)   # Output: 25


# but as we know A class method doesn’t directly access or modify instance variables (like self.name or self.age) because it works at the class level
# and Its first parameter is cls, which refers to the class itself (e.g., Person), not an instance (like self)
# However, a class method can still create an instance and indirectly set instance variables by calling the class’s constructor (like __init__) and returning that instance. 
# That’s what’s happening in the example


# cls(name, int(age)) acts like Person(name, int(age))
# This calls the __init__ method behind the scenes
# which does set the instance variables (self.name and self.age)

# consider cls as class name and (name, int(age)) as the arguments to the constructor of the class

