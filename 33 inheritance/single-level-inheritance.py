# <!-- *** Single level inheritance *** -->

# in Python Inheritance is a fundamental concept in object-oriented programming (OOP) that allows one class to inherit attributes and methods from another class
# In Python this means a new class (called a subclass or derived class) can reuse 
# and extend the functionality of an existing class (called a base class or parent class) without rewriting the code

# <!-- How Inheritance Works -->
# <!-- The subclass inherits all the methods and attributes of the parent class. -->
# <!-- You can also override or extend the inherited behavior by defining new methods or redefining existing ones in the subclass. -->

# types of inheritance in Python
# 1. Single level inheritance
# 2. Multi-level inheritance
# 3. Multiple inheritance
# 4. Hierarchical inheritance
# 5. Hybrid


# a single level inheritance is when a class inherits from only one class
# means a subclass or childe class inherits from only one parent class


# example 

# Creating a parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print("Hello!")

# this is the parent class
# it has two attributes name and age
# and a method say_hello

# Creating a child class
class Student(Person):
    def __init__(self, name, age, student_id):
        # calling the parent class constructor
        super().__init__(name, age)# --- the supper() function is used to call the constructor of the parent class
        # not only the counstructor but also the methods and attributes of the parent class can be called using the super() function
        self.student_id = student_id

    def study(self):
        print(f"{self.name} is studying") # using the name attribute of the parent class

# this is the child class
# it inherits from the parent class
# it has an additional attribute student_id
# and a method study

# Creating an object of the child class
student = Student
student.study() # Output: Alice is studying
student.say_hello() # Output: Hello! -- the method of the parent class can be called using the object of the child class
 
# In this example, the Student class inherits from the Person class
# The Student class has all the attributes and methods of the Person class
# The Student class also has an additional attribute student_id and a method study

# The super() function is used to call the constructor of the parent class
# It initializes the name and age attributes of the Person class
  
# the inheritance is a very useful concept in OOP
# it helps to avoid code duplication means we can reuse the code of the parent class in the child class
