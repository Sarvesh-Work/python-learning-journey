# *** Hybrid inheritance ***

# this inheritance combines two or more types of inheritance such as single multiple multilevel or
# hierarchical inheritance within a single program 
# Its like a mix-and-match approach to inheritance allowing a class to inherit properties and behaviors from multiple parent classes in a flexible way


# consider the example ----

# a Person class might serve as a base class with basic attributes like name and age
# a Student class inherits from Person (single inheritance)
# a Teacher class also inherits from Person (hierarchical inheritance)
# now a TeachingAssistant class might inherit from both Student and Teacher (multiple inheritance) creating a hybrid structure

class Person:
    def __init__(self, name):
        self.name = name
    
    def display(self):
        print(f"Name: {self.name}")

class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id
    
    def show_student(self):
        print(f"Student ID: {self.student_id}")

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
    
    def show_teacher(self):
        print(f"Subject: {self.subject}")

class TeachingAssistant(Student, Teacher):
    def __init__(self, name, student_id, subject):
        Student.__init__(self, name, student_id)
        Teacher.__init__(self, name, subject)

# Example usage
ta = TeachingAssistant("Alex", "S123", "Math")
ta.display()         # From Person
ta.show_student()    # From Student
ta.show_teacher()    # From Teacher