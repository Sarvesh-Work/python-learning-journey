# *** method overriding ***
# Method overriding is a feature that allows a subclass to provide a specific implementation of a method that is already provided by its parent class
# in simple words, a subclass can provide
# a specific implementation of a method that is already provided by its parent class
#
# # example

# Creating a parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print("Hello!")

# Creating a child class
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def say_hello(self):
        print("Hi!")  # overriding the say_hello method of the parent class

# Creating an object of the child class
student = Student("Alice", 20, 101)
student.say_hello()  # Output: Hi!
# In this example, the Student class overrides the say_hello method of the Person class
# The Student class provides a specific implementation of the say_hello method
# When you call the say_hello method using the student object, the implementation of the Student class is used
# Method overriding is useful when you want to provide a different implementation of a method in the subclass
# It allows you to customize the behavior of the method for the subclass