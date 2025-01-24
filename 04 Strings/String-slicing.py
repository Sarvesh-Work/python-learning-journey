# *** String Slicing **

# consider this string
names = "alex,joy"

# find the length of the string using len()
print(len(names))  # This will output 8, as there are 8 characters in the string including the comma

# String slicing to extract 'alex'
# syntax: string[start:end] where 'start' is the index of the first character, and 'end' is the index where slicing stops (the ending index will not be consider).
print(names[0:4])  # Outputs 'alex'. It slices the string from index 0 to index 3including the character at index 0, but excluding the character at index 4

# Negative slicing
# Negative indices allow you to count backwards from the end of the string.
# Example: -1 refers to the last character, -2 to the second-to-last character, and so on.
print(names[0:-5])  # Outputs 'alex'. This slices the string from index 0 up to 5 characters from the end but excluding the last 5 characters ('joy' and the comma)
