# *** Magic/Dunder Method ***

# Magic methods are special methods that have double underscores at the beginning and end of their names
# They are also called dunder (double underscore) methods
# They allow you to emulate the behavior of built-in objects
# They are commonly used in operator overloading, type conversion, and customizing object behavior

# example
# __init__ method
# It’s called when an instance of the class is created
# It initializes the instance variables of the class
# It’s a constructor

# __str__ method
# It’s called when you use the print() function or str() to convert an object to a string
# It returns a string representation of the object
# It’s used to display information about
# the object

# __add__ method
# It’s called when you use the + operator to add two objects
# It defines the behavior of the + operator for the class
# It allows you to customize the addition operation

# __len__ method
# It’s called when you use the len() function to get the length of an object
# It returns the length of the object
# It allows you to customize the len() function for the class

# __getitem__ method
# It’s called when you access an item from an object like a list or dictionary
# It allows you to customize the behavior of the [] operator
# It’s used to get an item from the object

# __setitem__ method
# It’s called when you set an item in an object like a list or dictionary
# It allows you to customize the behavior of the [] operator
# It’s used to set an item in the object


# example
# Creating a custom class
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # __str__ method
    def __str__(self):
        return f"{self.title} by {self.author}"

    # __len__ method
    def __len__(self):
        return self.pages

    # __getitem__ method
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "pages":
            return self.pages
        else:
            return None

    # __setitem__ method
    def __setitem__(self, key, value):
        if key == "title":
            self.title = value
        elif key == "author":
            self.author = value
        elif key == "pages":
            self.pages = value


# Creating an object of the Book class
book = Book("Python Programming", "Alice", 300)

# Using the __str__ method
print(book)  # Output: Python Programming by Alice -- the __str__ method is called when you use the print() function

# Using the __len__ method
print(len(book))  # Output: 300 -- the __len__ method is called when you use the len

# Using the __getitem__ method
print(book["title"])  # Output: Python Programming -- the __getitem__ method is called when you access an item using []

# Using the __setitem__ method
book["title"] = "Java Programming"  # the __setitem__ method is called when you set an item using []
print(book["title"])  # Output: Java Programming

# there are many other magic methods in Python that you can use to customize the behavior of your objects
# this are some of the most commonly used magic methods

