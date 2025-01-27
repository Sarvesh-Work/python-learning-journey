# *** raising custom error using raise keyword ***


# we can raise custom error using raise keyword
# and show the error message that we want to show 

# consider 
# that we are taking the number form user 
# and  showing that if the number is greater than 9 it is invalid
# and less than 5 is also invalid

number=int(input("Enter a number: "))
if(number<5 | number>9 ):
    raise ValueError(f"number is invalid : {number}")
else:
    print("you can continue")

# raise is a keyword that throws the custom error 
# now if user enter the number 10 
# the code will or the raise key word raise an error 
#       ValueError: number is invalid : 10 --this error 

  
