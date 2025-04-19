# A generator is a special type of function in Python 
# that remembers its state and yields values one at 
# a time instead of returning all at once



# imagine you have to process a huge list of numbers (like 1 to 1 billion)
# If you create a normal list, it takes a lot of memory
# A generator gives you one number at a time only when needed, saving memory and improving performance

# here we uses yeild insted of return 

# yeild : yield pauses the function and saves its place, so it can continue from there the next time you call it


# ex ---->


def count(n):
    count =1 
    for i in range(n):
        if i <= count:
            yield i
            count +=1


for i in count(10):
    print(i)