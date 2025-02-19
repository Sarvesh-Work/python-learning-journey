# *** class methods ***

# In Python, a class method is a method that belongs to the class itself rather than to any individual object
# It can access and modify class variables but cannot access instance variables directly

# ky points -->
#    Belongs to the class, not an instance
    #  Does not use self, but instead uses cls (class reference)

# Uses the @classmethod decorator
# This tells Python that the method should be called on the class, not on an instance

# ex-->

class Car:
    wheels = 4  # Class variable (shared by all instances)

    def __init__(self, color):
        self.color = color  # Instance variable (specific to each object)

    @classmethod
    def change_wheel_count(cls, new_wheels): # --- cls refers to the class not the current  instance
        cls.wheels = new_wheels  # Modifies the class variable the global variable  shared by all the class objects 

# Create objects
car1 = Car("Red")
car2 = Car("Blue")

# Default wheel count (before calling class method)
print(car1.wheels)  # 4
print(car2.wheels)  # 4

# Change wheels using class method
Car.change_wheel_count(6)

# Now all objects have updated wheel count
print(car1.wheels)  # 6
print(car2.wheels)  # 6



# +----------------+------------+------------+---------------------------+------------------+----------------------------+
# | Method Type    | Uses self? | Uses cls?  | Can access instance vars? | Can access class vars? | Modifies class vars? |
# +----------------+------------+------------+---------------------------+------------------+----------------------------+
# | Instance Method| ✅ Yes     | ❌ No     | ✅ Yes                    | ✅ Yes          | ✅ Yes                     |
# | Class Method   | ❌ No      | ✅ Yes    | ❌ No                     | ✅ Yes          | ✅ Yes                     |
# | Static Method  | ❌ No      | ❌ No     | ❌ No                     | ❌ No           | ❌ No                      |
# +----------------+------------+------------+---------------------------+------------------+----------------------------+





   