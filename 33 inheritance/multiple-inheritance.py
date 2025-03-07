# *** Multiple Inheritance ***
# Multiple inheritance allows a class to inherit attributes and methods from multiple parent classes.
# Python fully supports this, unlike languages like Java that restrict it.

class Person1:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        return f"Name of Person1 is {self.name}"


class Person2:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        return f"Name of Person2 is {self.name}"


class Child(Person1, Person2):  # Descriptive name, follows Python conventions
    def __init__(self, name):
        # explicitly initialize both parents (optional if they set the same attribute)
        Person1.__init__(self, name)
        # Person2.__init__(self, name)  # Uncomment if Person2 has unique initialization

    def combined_names(self):
        # explicitly combine both parents methods
        return f"{Person1.show_name(self)} | {Person2.show_name(self)}"


# Create instance
obj = Child("Sarvesh")


print(obj.show_name())  # calls Person1s show_name due to order (Person1, Person2)

# Show combined output from both parents
print(obj.combined_names())


print(Child.mro()) #this returns order of execution