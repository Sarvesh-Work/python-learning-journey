# *** Access Modifiers ***

# in python access modifiers are used to control the visibility or accessibility of class attributes and methods
#  Unlike some other languages (like Java or C++), Python doesn't have strict access modifiers
#  However it follows a convention that helps define what should be "public" or "private."

# 1. public access modifier
# Public members are accessible from anywhere both inside and outside the class
# public attributes are normal attributes
# like a="10"  -- this is a normal or public variable 
# ex-->  

class person :
    def _init_(self,name):
        self.name=name #---- public variable

    def greet():  #---- public method   
        print("hello")


# the variable and methods present in the person class are public members
p=person("sam")
print(p.name) #--- > accessing public name variable 
p.greet() #--- > accessing public method greet


# 2  protected access modifier
# the protected members are only used in the same class and there sub class means childe class
# In python there no true protection  but conventionally an attribute or method with a single underscore (_) is considered protected
# Protected attributes should not be accessed directly outside the class or subclass  but they can be if necessary

# lets take same example
class person2 :
    def _init_(self,name):
        self._name=name #---- protected variable

    def _greet():  #---- protected method   
        print("hello")


h = person2("Alice")
print(h._name)  # Not recommended, but works
h._greet()  # Not recommended, but works

# here we have created the protected variable and method 
#now the _ means they are protected means we cannot access the directly outside the class
# but it only a convention and the attribute is still accessible from outside the class

# 3   private access modifier
# now the private variables are the variables which only accessible inside its own class 
# not outside or childe class 
#  Python private members are indicated by a double underscore (__) before an attribute or method name
#  This makes Python mangle the name to prevent accidental access

# mangle --> Name mangling is a mechanism in Python that modifies the names of private attributes (those with a double underscore __) to make them harder to access from outside the class
# means if we have variable like name which is private with __name the python mangling mechanism rename it to person_name variable name with class name 

# lets see 
# ex--->

class Person:
    def __init__(self, name):
        self.__name = name  # Private attribute

    def __greet(self):  # Private method
        return f"Hello, my name is {self.__name}"

# now this is the class which has private members 
# we cannot access private members outside or  any where 

# so if we try accessing them directly
# print(p.__name)  #  AttributeError: 'Person' object has no attribute '__name'
# print(p.__greet())  #  AttributeError
# it will throw error

# but still we can access them 
# with  name Mangling: Accessing private attributes using the modified name
print(p._Person__name)  #  Works, but not recommended
print(p._Person__greet())  #  Works, but not recommended

# Name mangling is NOT real security – it just discourages direct access
# name mangling only works for private access modifiers means only for double (__) underscore
# we  should avoid using mangled names (eg:person_name) directly – use getters and setters instead 


# now there one special case also 
# which is _slot_

# 4 _slot_
# we can use slot when we want to restrict the creation of new attributes dynamically (i.e., outside of the class definition) we can use __slots__
# This is a way to define a fixed set of attributes for the object

class Person:
    __slots__ = ['name', 'age']  # Limit the attributes to 'name' and 'age'

    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Alice", 25)
# p.address = "123 Street"  # AttributeError: 'Person' object has no attribute 'address'

# With __slots__ you cant dynamically add new attributes ensuring that the objects attributes are tightly controlled