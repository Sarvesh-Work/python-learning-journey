# *** Time Module ***

# The time module is a built-in Python module that provides various time-related functions
# basically  we  use time module when we have to perform any time related task 


import time  #--- to us time module we import it

# 1
print(time.time())
# Returns current time as a floating-point number in seconds since epoch (Jan 1, 1970)

# 2
time.sleep(3) #--- 3  seconds
# Suspends execution for the given number of seconds

# 3
print(time.ctime())  # Example: "Wed Mar 12 10:00:00 2025"
# Converts time in seconds to a readable string


# 4

local_time = time.localtime()
print(local_time.tm_year)  # Access year: 2025
print(local_time.tm_mon)   # Access month: 3

# Returns a struct time object with local time

#5

formatted = time.strftime("%Y-%m-%d %H:%M:%S")
print(formatted)  # Example: "2025-03-12 10:00:00"
# Formats time according to specified format