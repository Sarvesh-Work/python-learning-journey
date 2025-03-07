# *** hierarchical ***

# in this a single base (parent) class is inherited by multiple derived (child) classes 
# Think of it like a family tree branching out from one ancestor the base class provides common functionality and each child class adds its own specialized features

# a hierarchical  means a main parent class set a top and Multiple child classes inherit directly from that parent
# and those children can have a multiple children of there own


class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!")

class Bird(Animal):
    def speak(self):
        print(f"{self.name} says Chirp!")

# Example usage
dog = Dog("Buddy")
cat = Cat("Whiskers")
bird = Bird("Tweety")

dog.speak()   # Output: Buddy says Woof!
cat.speak()   # Output: Whiskers says Meow!
bird.speak()  # Output: Tweety says Chirp!