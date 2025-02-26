# *** Operator Overloading ***

# Operator overloading allows you to redefine how operators (e.g., +, -, *) behave with custom objects.
# By default, operators work with built-in types like integers (2 + 3) or strings ("hello" + "world").
# With operator overloading, you can customize their behavior for your own classes, teaching Python how to handle them.

# Example: Adding two custom objects

class Add:
    def __init__(self, a, b):
        self.a = a  # First value
        self.b = b  # Second value

    def __str__(self):
        # Returns a string representation with values and their sum
        return f"Values: {self.a}, {self.b} | Sum: {self.a + self.b}"

    def __add__(self, x):
        # Overrides the + operator to add corresponding attributes of two objects
        return f"{self.a + x.a}, {self.b + x.b}"  # Returns a string with added values

# Create objects
a1 = Add(4, 5)  # First object
print(f"1st object: {a1}")  # Calls __str__ to display object details

a2 = Add(7, 9)  # Second object
print(f"2nd object: {a2}")  # Calls __str__ for second object

# Add the objects using the + operator
print(f"Result of a1 + a2: {a1 + a2}")  # Calls __add__ to combine a1 and a2

# Output:
# 1st object: Values: 4, 5 | Sum: 9
# 2nd object: Values: 7, 9 | Sum: 16
# Result of a1 + a2: 11, 14