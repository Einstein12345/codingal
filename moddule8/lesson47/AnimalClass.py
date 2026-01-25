#Write a program to implement abstraction
#  on animal class (base class). The abstract
#  method will be move that is for
#  displaying what subclasses can do.
from abc import ABC,abstractmethod

class animal(ABC):
    def move(self):
        pass

class Dog(animal):
    def move(self):
        print("i can bark")    
class Lion(animal):
    def move(self):
        print("i can roar") 
d=Dog()
d.move()
l=Lion()
l.move()                  