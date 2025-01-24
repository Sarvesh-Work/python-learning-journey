# Dictionaries Methods

#1. update()
# this method updates the dictionary with elements from another dictionary object or from an iterable object of key-value pairs
dict1 = {"name": "John", "age": 25, "city": "New York"}
dict2 = {"country": "USA", "profession": "Engineer"}
dict1.update(dict2)
print(f"The updated dictionary is {dict1}.") # output={'name': 'John', 'age': 25, 'city': 'New York', 'country': 'USA', 'profession': 'Engineer'}
# it combines both the dictionaries

#2. pop()
# this method removes the item with the specified key name
dict1.pop("city")
print(f"The updated dictionary is {dict1}.") # output={'name': 'John', 'age': 25, 'country': 'USA', 'profession': 'Engineer'}


#3. clear()
# this method empties the dictionary
dict1.clear()
print(f"The updated dictionary is {dict1}.") # output={}

#4. copy()
# this method returns a copy of the dictionary
dict1 = {"name": "John", "age": 25, "city": "New York"}
dict2 = dict1.copy()
print(f"The copied dictionary is {dict2}.") # output={'name': 'John', 'age': 25, 'city': 'New York'}

#5. popitem()
# this method removes the last inserted item and returns it 
dict1.popitem()
print(f"The updated dictionary is {dict1}.") # output={'name': 'John', 'age': 25}

#6 len()
# returns the number of key-values pairs in the dictionary
print(f"The length of the dict {len(dict1)} ") # output=2


