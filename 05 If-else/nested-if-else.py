

#! example for nested if-else

# If the number of apples is exactly 4, check if the apples are organic:
# If organic, the price is 90.
# If not organic, the price is 80
# For other quantities, the price logic remains as before

# number of apples and whether they are organic
apple = 4
is_organic = True

# Using nested if-elif-else
if apple < 4:
    print(50)  # Price for less than 4 apples
elif apple == 4:
    if is_organic:
        print(90)  # Price for exactly 4 organic apples
    else:
        print(80)  # Price for exactly 4 non-organic apples
else:
    print(100)  # Price for more than 4 apples/
