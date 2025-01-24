# *** Dictionary ***

# Dictionary is a collection of key-value pairs.
# Dictionary is mutable.
# Dictionary is ordered. -- from Python 3.7
# Dictionary is indexed.
# Dictionary is represented by curly braces {}.

# npr mal example

dict1 = {"name": "John", "age": 25, "city": "New York"}
# this is the dictionary

#  Accessing Items
# you can access the items of a dictionary by referring to its key name
# you can use the key inside square brackets []
print(f"The name of the person is {dict1['name']}.") # output=John

# adding Items 
dict1["center"]="world"
print(f"The new item is added in dict1 {dict1}")

#  Changing Items
# you can change the value of a specific item by referring to its key name
dict1["age"] = 30
print(f"The age of the person is {dict1['age']}.") # output=30

# to access only the keys of the dictionary
keys = dict1.keys()# --- it will return a list of keys
print(f"The keys of the dictionary are {keys}.") # output=['name', 'age', 'city'] --- in list format

# to access only the values of the dictionary
values = dict1.values()# --- it will return a list of values
print(f"The values of the dictionary are {values}.") # output=['John', 30, 'New York

# to access both the keys and values of the dictionary
items = dict1.items()# --- it will return a list of tuples
print(f"The items of the dictionary are {items}.") # output=[('name', 'John'), ('age', 30), ('city', 'New York')]

# iterating  dictionary
for key, value in dict1.items():
    print(f"The {key} is {value}.")




