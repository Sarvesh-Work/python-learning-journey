# --- Strings in Python ---

# Strings in Python are used to store text and can be enclosed in either single (' ') or double (" ") quotes.
# Both are valid ways to define a string

# Example: String with double quotes
name = "sarvesh"  # String stored in double quotes
print(name)  # Output: sarvesh

# Example: Multiline string using triple quotes (either ''' or """ can be used)
paragraph = ''' 
Hi, I am Alex. 
I am 34 years old. 
I have a car. 
I drink water. 
'''

print(paragraph)

# --- Accessing String Characters by Index ---
# In Python, strings are indexed starting at 0. You can access individual characters by specifying the index.
# Indexing starts at 0 for the first character.

name2 = "alex"
print(name2[0])  # Output: 'a' (the character at the 0th position in the string "alex")

# You can also access other characters by specifying different indices:
print(name2[1])  # Output: 'l' (the character at the 1st position)
print(name2[2])  # Output: 'e' (the character at the 2nd position)

# --- Negative Indexing ---
# Python also supports negative indexing, where -1 refers to the last character, -2 to the second-to-last, and so on.

print(name2[-1])  # Output: 'x' (the last character in the string "alex")
