# *** Import - keyword ***

# Import keyword is used to import modules into the current namespace.
# it is used to import pre-defined modules as well as user-defined modules.


# lest use built in module math as an example

import math # import math module -- this is the one way of importing a module

# now we can use "math" module to access its functions
# like this-----
print(math.sqrt(25)) # 5.0
print(math.pi) # 3.141592653589793
 
# this are some predefined functions in math module
# sqrt() - returns the square root of a number
# pi - returns the value of pi
# etc.



from math import sqrt,pi # import math module -- this is the another way of importing a module
# this is use to import only specific functions from a module

# now we can directly use sqrt() and pi() functions without using math. prefix
# like this-----
print(sqrt(25)) # 5.0
print(pi) # 3.141592653589793

# there is another way of importing a module
# like this-----

from math import * # this will import all the functions from math module
# now we can directly use all the functions without using math. prefix
# like this-----
print(sqrt(25)) # 5.0
print(pi) # 3.141592653589793

# *Note: It is not recommended to use this way of importing a module because it may cause name conflicts with other modules.

# we can also import a module with an alias name -- means we can give a different name to the module or its functions
# like this-----
import math as m # here we are giving alias name m to math module
# now we can use m instead of math
# like this-----
print(m.sqrt(25)) # 5.0
print(m.pi) # 3.141592653589793

# we can also import specific functions with alias name
# like this-----
from math import sqrt as s, pi as p # here we are giving alias name s to sqrt() and p to pi()
# now we can use s instead of sqrt() and p instead of pi()
# like this-----
print(s(25)) # 5.0
print(p) # 3.141592653589793


# lets see an example of user-defined module
# now i have created a module named user-define.py
# which contains a function hi() which prints "Hello, World!"

# lets import this module and use its function
import user_define # type: ignore # import user_define module

# now we can use hi() function from user_define module
# like this-----
user_define.hi() # Hello, World!

# *Note: user_define.py file should be in the same directory as this file
# if it is not in the same directory then you have to provide the path of the file
# like this-----
# import sys
# sys.path.append('path of the file')

