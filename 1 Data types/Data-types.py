# ** Data Types in Python **

# Number Types: int, float, complex (includes real and imaginary parts)
# Mapping Type: dict
# Boolean Type: bool (can only be True or False)
# Sequence Types: str (string), list, tuple, range
# Set Types: set, frozenset
# Binary Types: bytes, bytearray
# None Type: NoneType

# These are all the data types in Python.

# ---- Variables ----
# A variable is a named reference to a memory location that stores data.
# It acts as a container to hold values provided by Python.

# --- String Data Type ---
name = "alex"  # Example of a string

# --- Integer Data Type ---
age = 23  # Example of an integer

# --- Float Data Type ---
height = 6.5  # Example of a float

# --- Boolean (bool) Data Type ---
male = True  # Example of a boolean

# --- List Data Type ---
# A list can store a collection of items of different data types.
numbers_list = [1, 3, 5, 6, 7]  # Example of a list

# --- Tuple Data Type ---
# Tuples are immutable (cannot be changed after declaration).
colors_tuple = (
    ("alex", "pink", "green", "blue"),
    ("black", "white"),
)  # Example of a tuple

# --- Dictionary (dict) Data Type ---
# A dictionary is an unordered, changeable, and indexed collection.
person_dict = {
    "name": "sarvesh",
    "age": 20,
}  # Example of a dictionary

# ---- Printing and Type Checking ----
# Using the print() function to display values
print(name)  # Output: alex

# Using the type() function to check the type of a variable
print(type(male))  # Output: <class 'bool'>
