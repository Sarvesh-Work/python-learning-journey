# File Handling in Python
# Python provides built-in functions for reading, writing, appending, and managing files.


# 1. Reading a File (Standard Way)


# Opening a file using the traditional method (not recommended due to manual closing)
f = open("hello.txt", 'r')  # 'r' mode opens the file in read mode
text = f.read()  # Reads the entire file content
f.close()  # Always close the file to free resources
print(text)

# 2. Reading a File (Recommended Way using 'with')


# Using 'with open' ensures the file closes automatically after execution
with open("hello.txt", 'r') as f:
    text = f.read()  # Reads the file content
    print(text)  # Prints the content


# 3. Writing to a File (Overwrites Content)


# 'w' mode writes to the file, overwriting any existing content
with open("hello.txt", 'w') as f:
    f.write("Hi, hello!")  # This will replace previous content with "Hi, hello!"


# 4. Appending to a File (Adds Content Without Overwriting)


# 'a' mode appends new content at the end of the existing file
with open("hello.txt", 'a') as f:
    f.write(" Working on Python.")  # This adds content without removing existing data


# 5. Reading a File Line by Line (Using readline())


# Reading the file line by line and extracting only the first part before a comma
with open("hello.txt", 'r') as f:
    for line in f:
        first_part = line.split(',')[0]  # Extracting the part before the comma
        print(first_part)  # Printing only the first part of each line


# 6. File Pointer Operations (seek() and tell())


# seek() - Moves the file pointer too a specific position before reading
# tell() - Returns the current position of the file pointer

# Assume 'hello.txt' contains:
# "Hello everyone, how are you?" -- gist example

with open("hello.txt", 'r') as f:
    f.seek(5)  # Moves the pointer 5 characters forwarde
    text = f.read()  # Reads the rest of the file from position 5 onwards
    print(text)  # Output: " everyone, how are you?"
    
with open("hello.txt", 'r') as f:
    f.seek(5)
    print(f.tell())  # Output: 5 (current pointer position before reading)
    text = f.read()  # Reads the file from position 5
    print(f.tell())  # Output: Total characters in the file (pointer moves to the end)


# 7. Truncating a File (truncate())


# truncate() - Cuts the file to a specific size (removes extra content)

# Before truncating, assumee 'hello.txt' containse: "Hello everyone, how are you?"
with open("hello.txt", 'r+') as f:  # 'r+' allows reading and writing
    f.truncate(5)  # Keeps only the first 5 characters and removes the rest
    f.seek(0)  # Move back to the beginning of the file to read the content
    text = f.read()  # Read the truncated file content
    print(text)  # Output: "Hello"
