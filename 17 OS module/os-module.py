# *** os-module ***

# OS module is a built-in module in python which provides a way to interact with the operating system.
# It provides a way to use the operating system dependent functionality.
# The functions that the OS module provides allows you to interface with the underlying operating system that Python is running on – be that Windows, Mac or Linux.

import os # import os module

# now we can use "os" module to access its functions

# os.name - returns the name of the operating system dependent module imported
print(os.name) 

# os.getcwd() - returns the current working directory
print(os.getcwd())

# os.listdir() - returns the list of files and directories in the specified directory
print(os.listdir())

# os.mkdir() - creates a directory
os.mkdir("new_dir") # this will create a new directory named new_dir

# os.rmdir() - removes a directory
os.rmdir("new_dir") # this will remove the directory named new_dir

os.remove("file.txt") # this will remove the file named file.txt

os.rename("old.txt", "new.txt") # this will rename the file named old.txt to new.txt


os.path.exists("file.txt")

os.path.isfile("file.txt") # returns True if the file exists and is a file

os.path.isdir("new_dir") # returns True if the directory exists and is a directory

os.path.join("dir", "file.txt") # joins the path components

os.path.abspath("file.txt") # returns the absolute path of the file

os.path.basename("file.txt") # returns the base name of the file

os.path.dirname("file.txt") # returns the directory name of the file

os.path.split("dir/file.txt") # returns a tuple of the directory name and the base name of the file

os.path.splitext("file.txt") # returns a tuple of the file name and its extension

# etc.
