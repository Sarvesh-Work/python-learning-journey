# *** multilevel inheritance ***

# in multilevel inheritance a derived class inherits from a base class  and then another class inherits from that derived class creating a vertical hierarchy
# each level can add or override functionality
# in simple words it means that parent a having child b and childe b have another childe c

# ex----

# Base class (Grandparent)
class Grandparent:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} says: Hello from Grandparent!")

# Derived class (Parent) inheriting from Grandparent
class Parent(Grandparent):
    def work(self):
        print(f"{self.name} says: I am working hard!")

# Derived class (Child) inheriting from Parent
class Child(Parent):
    def play(self):
        print(f"{self.name} says: I am playing!")

# Create an instance of Child
child = Child("Sarvesh")
child.speak()  # from Grandparent
child.work()   # from Parent
child.play()   # from Child