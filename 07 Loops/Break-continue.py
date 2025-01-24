# *** break and continue ***

# break --- statement is used to exit the current loop entirely when a condition is met
# continue --- statement skips the current iteration of the loop and moves to the next one

# ex: Printing the multiplication table of 2 but stopping after 10 iterations
for i in range(1, 13):  # Start from 1 and go up to 12
    if i == 11:  # stop the loop when i reaches 11
        break
    print(f"2 x {i} = {2 * i}")

# ex: Using continue to skip a specific condition
print("\nSkipping multiples of 3:")
for i in range(1, 13):  # start from 1 and go up to 12
    if i % 3 == 0:  # skip multiples of 3
        continue
    print(f"2 x {i} = {2 * i}")
