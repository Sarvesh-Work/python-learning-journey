# *** Walrus operator ***

# The walrus operator in Python is used for assignment expressions
# It allows you to assign a value to a variable as part of an expression, making your code more concise and readable
# := this is walrus operator

# ex ---->

# consider we have a list
my_list=[3,4,5,6,7]

n = len(my_list)  # Assigning value
if n > 5:         # Using the value
    print("List is long!")

# and we write normal code like this here code is simple but we can make it more simple 

# instead  of doing  n = len(my_list)  this separately we can do it in if condition / expression

if (n:= len(my_list)) >5: #using walrus operator
    print("List is long!")

 # Here n is assigned len(my_list) and its value is used immediately in the condition