import asyncio

# asyncio is a Python library introduced in Python 3.4 to handle asynchronous programming. It allows you to write code that can run tasks concurrently, which is especially useful for operations that involve waiting, like:

# Making HTTP requests to APIs.
# Reading/writing to files or databases.
# Handling network connections (e.g., servers or clients).


# Normally, Python runs code line by line. If one line takes time (like downloading something), everything else waits.

# With async/await, Python can pause the slow task, go do something else, and then come back when the task is ready.

# ex --->
# we can define  async function using async keyword  this function can paused and resumed 

async  def say_hello():
    print("hello")


#await tells python wait here but menwhile feel free to do other stuff 

# ex --->

async def say_hello(): # async use to define  the funtion that can be stoped or restart 
    print("hello")
    await asyncio.sleep(2) # waits for 2 seconds without blocking  other execution 
    print ("World")


async def main():
    await say_hello()

asyncio.run(main())  #---> this is use to start running our async code 