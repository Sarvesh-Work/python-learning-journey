# *** Class , Objects and constructor ***

# Class
# A class in Python is like a blueprint for creating objects
# It defines how an object should behave and what properties (attributes) and actions (methods) it should have
# Think of a class like a design plan for a car.
# the plan itself is not a car, but we can use it to create multiple cars with similar features

# The same goes for a class; it acts as a structure/template that we can use to create objects
# We create a class using the 'class' keyword

# Object
# an object in Python is an instance of a class
# It is a real-world entity that contains both data (attributes) and behavior (methods)
# Think of a class as a blueprint and an object as the actual thing created from that blueprint
# for example, if we have a class called Car, we can create multiple objects (like a Toyota, a Honda, etc.) using that class

# --- Example ---->

# Consider we want to store or take multiple user data
# In normal or procedural programming, we can do it like this:

name="rock"
age=20
mob_no=901838393939

# Now if we want to create another user we have to define it again:

name2="sam"
age2=45
mob_no2=2829202020

# This approach works for a few users  but what if we have to create 100 users
# This method is inefficient and unorganized 
# In this scenario, using a class and objects is a better approach

# --- Converting the same example using Class and Objects ---->

# Creating a class

# 'student' is the name of the class
class student:
    name = "student_name"
    age = 20
    mob_no = 881919191

# Now we have created the 'student' class

# We can directly access the student class using its name:
print(student.name)  # Printing the default name present inside the student class

# We are printing the default values (initial values)
# Now, if we want to create our own user, we need to create an object of that class

# Creating an object of the student class
student1 = student()  # Creating an object

# Now using this object, we can initialize new values for the attributes in the class.
student1.name = "rock"
student1.age = 20
student1.mob_no = 18913030

# If we need to create another student, we can do it in the same way

# Creating another object of the student class
student2 = student()

student2.name = "sam"
student2.age = 45
student2.mob_no = 2829202020

# Like this we can create 100 or 1000 students easily without repeating the variable declarations.

# --- Understanding Instances ---
# Each object (student1, student2, etc.) is called an **instance** of the class
# An instance is a unique copy of the class with its own set of attribute value
# Although they share the same blueprint (class), their data is independent

# Both student1 and student2 have different reference values in memory
print(id(student1))  # Unique memory address of student1
print(id(student2))  # Different memory address of student2

# This proves that each instance is separate and independent

# **Advantages of using Classes and Objects:**
# 1. Organizes data efficientl
# 2. Avoids repetition of code
# 3.  makes it easier to scale (handle thousands of users easily)
# 4. Each object (instance) has its own independent data


# constructor
# In Python a constructor is a special method used to initialize objects of a class
# It is defined using the __init__ method 
# The constructor is automatically called when a new instance/object of the class is created

# in simple words we use constructor to initalize the  variables of a class

# types of constructor
# there are 3 types of constructor 
# 1.Default constructor :A constructor with no parameters (except self), used for basic object creation.
#   self: self is use to point to the current object or current instance
# ex --->

class Student:
    def __init__(self):  # Default constructor
        print("Default Constructor Called!")

# Creating an object
s1 = Student()  # Output: Default Constructor Called!


# 2.Parameterized Constructor
# a constructor that takes arguments to initialize object attributes


class Student:
    def __init__(self, name, age):  # Parameterized constructor
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating an object
s1 = Student("Alice", 20)
s1.display()  # Output: Name: Alice, Age: 20


# 3. constructor with Default Arguments
# Allows optional parameters with default values.

class Student:
    def __init__(self, name="Unknown", age=18):# --> default values
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

s1 = Student()  # Uses default values
s1.display()  # Output: Name: Unknown, Age: 18

s2 = Student("Bob", 22) #not default values
s2.display()  # Output: Name: Bob, Age: 22
