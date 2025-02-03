# *** is vs == in Python ***

# The `is` operator checks **whether two variables reference the same object in memory (identity comparison)
# The `==` operator checks **whether two variables have the same value (value comparison)

# Example 1: `is` checks memory location (object identity)
a = 10
b = a  # `b` refers to the same memory location as `a`

print(a is b)  # Output: True  (Both refer to the same object)
print(a == b)  # Output: True (Both have the same value)

# Example 2: `is` vs `==` with integers outside the interned range (-5 to 256)
c = 800
d = 800

print(c == d)  # Output: True (Values are the same)
print(c is d)  # Output: False (Different objects in memory)

# Why is `c is d` False?
#  Python **caches small integers** (-5 to 256) for optimization.
#  Numbers outside this range (`> 256` or `< -5`) are **not cached** and stored as separate objects.
#  hence, `c` and `d` have the same value but are stored in **different memory locations**

# Example 3: `is` vs `==` with lists
list1 = [1, 2, 3]
list2 = [1, 2, 3]

print(list1 == list2)  # Output: True  (Values are the same)
print(list1 is list2)  # Output: False (Different memory locations)

# Lists are **mutable**, so Python stores them as separate objects, even if they have the same values

# Example 4: `is` vs `==` with strings
str1 = "hello"
str2 = "hello"

print(str1 == str2)  # Output: True  (Same values)
print(str1 is str2)  # Output: True (Python caches short strings for optimization)

# hsowever, if a string is created dynamically, `is` might return False:
str3 = "".join(["he", "llo"])
print(str1 == str3)  # Output: True  (Same value)
print(str1 is str3)  # Outputs: False (Different memory locations)

# Summary:
# use `is` when checking if two variables refer to the **same object in memory**
# use `==` when checking if two variables have the **same value**

