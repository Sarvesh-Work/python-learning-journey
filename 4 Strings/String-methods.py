#*** String methods in Python ***

# strings in Python are immutable. This means that once a string is created, it cannot be modified.
# in python instead of modifying the existing string, string methods return a new string with the desired changes.

# methods

#* 1 upper() and lower()

# The `upper()` method converts all characters in a string to uppercase.
# The `lower()` method converts all characters in a string to lowercase.

name = "alex"

# Convert to uppercase using upper()
uppercase_name = name.upper()
print(uppercase_name)  # Output: "ALEX"

# Convert to lowercase using lower()
lowercase_name = name.lower()
print(lowercase_name)  # Output: "alex"

# the original string remains unchanged
print(name)  # Output: "alex" 



#* 2 strip()

# the strip() method removes any leading (start) and trailing (end) whitespace from a string.
a=" hi "
print(a.strip() )  # Output: "hi" --- only hi without white space 



#* 3 replace()

#This method is use to replace  all occurrences of old with new in the string.
# in simple word it replaces old sting to new string 
b="hello world"
print(b.replace("world","hello"))  # Output: "hello hello"
print(b.replace("orld","hello"))  #--- this will also work  # Output: "hello whello"

#* 4 split()

# The split() method splits a string into a list based on a specified delimiter.
# for this the split method required the delimiter means the argument which tell the method from which string i have to split the string
c="alex working"
print(c.split(" ")) # -- here we are Split the string from white space but we can provide anything that the string contain      
# Output: [alex, work]



#* 5 Capitalizes()

# Capitalizes the first character of the string and makes the rest lowercase.
d="hi i am alex"
print(d.capitalize()) # Output: "Hi i am alex"



#* 6 count()

# the count method is use to count that how many times the given string is occurring in the main string
e="hi hi hi i am alex"
print(e.count("hi"))  # Output: 3 --- 3 times the hi is occurring




#* 7 endswith() startswith() --- here w is small of with

# Checks if the string starts or ends with a specific prefix or suffix.
# this method gives the out put in boolean / bool format true or false

f="hello world i am alex"
print(f.startswith("hello"))  # Output: True
print(f.startswith("Hello"))  # Output: False

print(f.endswith("alex"))  # Output: True
print(f.endswith("Alex"))  # Output: False

# Using endswith() with start and end indices to check a substring
# Here, checking if the substring from index 5 to 11 ends with "ld"
print(f.endswith("ld", 5, 11))  # Output: True

# also can do same thing using startswith


#* 8 find()

#Returns the index of the first occurrence of the substring. 
# Returns -1 if the substring is not found.

text = "Hello World"
print(text.find("World"))  # Output: 6
print(text.find("Python"))  # Output: -1 (not found)

#* 9 index()

# The `index()` method is used to find the first occurrence of a specified substring in a string.
# If the substring is not found, it raises a `ValueError`.

text2 = "Hello, world!"
# position = text.index("world")  # Finds the starting position of "world"
# print(position)  # Output: 7


#* 10 isalnum() and isalpha()

# ----isalnum()
# Returns True if the string contains only letters and numbers
# if a string  contains other than numbers and letters it will return false 
 
# isalpha()
# this returns true if the string contains only letters 
# if string contains other than letters it will return False

text3="alex"
print(text3.isalnum()) #true
print(text3.isalpha()) #true

#* 11 isprintable()

# this method is use to check the given string is printable or not 

word="hi"
print(word.isprintable()) #true

word="hi\n"
print(word.isprintable()) #false

#* 12  isspace()

# this method returns true if the string contains whitespace and false if not 
hi="    "
print(hi.isspace()) #true

#* 13 isTitle()

# it returns the true if the first letter of each word in string is capitalized else false

str1="Hi alex"
print(str1.istitle()) #false

str1="Hi Alex"
print(str1.istitle()) #true

#* 14 swapcase()

# this method is use to swap upper case string upper to lower and lower to upper

str2="hi"
print(str2.swapcase()) #output= HI

str2="Hi"
print(str2.swapcase()) #output= hi


#* 15  title()

# Converts the first character of each word to uppercase and the remaining characters to lowercase.
text4 = "hello world"
print(text.title())  # Output: "Hello World"




