# *** instance variable and class variable ***


# Instance Variable

# An instance variable is a variable that belongs to a specific object (also called an instance) of a class
#  Each object has its own copy of the instance variable and changing it does not affect other objects
# for each object creation it will have diffrenct value  

# ex--->
# consider
# a Car Factory where different cars are being built
# Each car has its own unique color and model


class Car:
    def __init__(self, color, model):
        self.color = color  # Instance variable
        self.model = model  # Instance variable

# Creating two car objects
car1 = Car("Red", "Toyota") #--> 1st object creation  has different values 
car2 = Car("Blue", "Honda") #--> 2nd has different values 

print(car1.color)  # Output: Red
print(car2.color)  # Output: Blue

# now here the color and the model is vary for each object creation and give the different output 
# according to the user input 

# this is called instance variable 


# class variable 

# A class variable is a variable that is shared by all objects of the class
# If you change a class variable the change will be reflected in all objects (unless overridden inside an object)

# in simple word class variable is common for all the object creation
# and if  we change it  that change will reflect in every object creation

# not-- you can think of it as static variable like java but we dont call it as static variable in python and it dose not use static keyword 



# ex --->

# consider In the  Car Factory all cars have 4 wheels by default
# This means the number of wheels is the same for every car

class Car:
    wheels = 4  # Class variable (shared by all cars)

    def __init__(self, color, model):
        self.color = color  # Instance variable
        self.model = model  # Instance variable

# Creating two car objects
car1 = Car("Red", "Toyota")
car2 = Car("Blue", "Honda")

print(car1.wheels)  # Output: 4
print(car2.wheels)  # Output: 4

# Changing class variable
Car.wheels = 6

print(car1.wheels)  # Output: 6
print(car2.wheels)  # Output: 6


# wheels is a class variable because all cars have the same number of wheels
# Changing Car.wheels = 6 affects all cars 
# Unlike instance variables  all objects share class variables