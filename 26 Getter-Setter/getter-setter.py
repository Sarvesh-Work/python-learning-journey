# *** Getter and Setter ***
#  getters and setters are used to control how we access and update the values of class attributes (variables inside a class) 
# they help encapsulate data  meaning we can protect attributes/variables  from being changed accidentally

# ex--> a example Without Getters and Setters

class Person:
    def __init__(self, name):
        self.name = name  # Public attribute

p = Person("Alice")
print(p.name)  # Direct access
p.name = "Bob"  # Direct modification
print(p.name)
# If we don’t use getters and setters we can directly access attributes 
# so here in this example any one can access the variable and update also easeyly
# to prevent  that we use setter and setter 


# now lets use Getter and Setter


class Person:
    def __init__(self, name):
        self._name = name  # Using _name (convention for private variables)

    def get_name(self):  # Getter
        return self._name

    def set_name(self, new_name):  # Setter
        if isinstance(new_name, str) and new_name.strip():
            self._name = new_name
        else:
            print("Invalid name!")

p = Person("Alice")
print(p.get_name())  # Access using getter
p.set_name("Bob")    # Modify using setter
print(p.get_name())

