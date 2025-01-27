# *** Enumerate ***

# Enumerate is a built-in function of Python. 
#  It allows us to loop over something and have an automatic counter. 
# Here is an example:

# Without enumerate
names = ['John', 'Doe', 'Jane']

for i in range(len(names)):
    print(i, names[i])


# With enumerate
names = ['John', 'Doe', 'Jane']

for index, name in enumerate(names):
    print(index, name)


# The enumerate() function takes a collection (e.g. a tuple) and returns it as an enumerate object.
# The enumerate() function adds a counter as the key of the enumerate object.
