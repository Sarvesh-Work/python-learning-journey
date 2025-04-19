from abc import ABC, abstractmethod

# Abstraction means hiding complex details 
# and showing only the essential features to the user

# to use abstraction on python we have to import ABC, abstractmethod
# from abc Abstract Base Classes


# ex --- >

class animal(ABC): # ---> abstractclass when we extends any class with ABC it becomes abstract class
     
     @abstractmethod  #--- > to make abstract method
     def make_sound(self):
          pass   #--- > this method implimentation will be don by the child class of animal
     


# child class

class cat(animal):
     
     def make_sound(self):
          return "meow"
     


class dog(animal):
     
     def make_sound(self):
          return "woof"


dog = dog()
cat = cat()

print(dog.make_sound())  # Woof!
print(cat.make_sound())  # Meow!