# *** if-elif-else in Python ***

# The "if-elif-else" statement is used when there are multiple conditions to check
# - if: Executes its block if the condition is True
# - elif (else if): Checks another condition if the previous if or elif was False.
# - else: Executes its block if none of the conditions are True.

# example:

# Let's decide the price based on the number of apples:
# - If the number of apples is less than 4 the price should be 50
# - if the number of apples is exactly 4 the price should be 80
# - If the number of apples is greater than 4 the price should be 100.

apple = 4  # number of apples

# Using if-elif-else to decide the price
if apple < 4:
    print(50)  # Price for less than 4 apples
elif apple == 4:
    print(80)  # price for exactly 4 apples
else:
    print(100)  # price for more than 4 apples

    # note--- if any condition matches it will execute that block  and ignore other conditions/blocks


