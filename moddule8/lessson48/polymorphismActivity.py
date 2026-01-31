#Polymorphism Implementation
#Outline:
#Write a program to create two classes Dog and Cat, with the same attributes - (name and age) and methods -
#  (info and make_sound). Create different objects for each class and pass the parameters. Showcase the 
# concept of polymorphism in this program
class cat:
    def __init__(self,name,age):
        self.name =name
        self.age =age
    def info(self):
        print(f"i am a cat.my name is {self.name}. i am {self.age} years old")
    def makeSound(self):
        print("meow")

class dog:
    def __init__(self,name,age):
        self.name =name
        self.age =age
    def info(self):
        print(f"i am a dog.my name is {self.name}. i am {self.age} years old")
    def makeSound(self):
        print("bark")    

Cat1=cat("Messi",5)
dog1=dog("ronaldo",2)

for animal in (Cat1,dog1):
    animal.makeSound()
    animal.info()