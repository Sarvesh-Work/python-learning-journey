# *** While Loop ***

# a while loop runs as long as the condition specified is true 
# in this example, we start with a number 0 and:
# - Print "hello" as long as the number is less than or equal to 4
# - Increment the number manually in each iteration
# - Use an else block to print "greater" when the condition becomes false

number = 0

while number <= 4:  # Loop continues while the condition is true
    print("hello")
    number += 1  # Incrementing the value manually
else:
    print("greater")  # Executes when the while loop condition becomes false


# Requires manual control of the loop variable (increment/decrement).
# it's not like for loop  for loop manage this automatically 