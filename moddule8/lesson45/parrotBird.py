#Write a program to create a class Parrot and perform the following tasks - Create a class variable species
#  Create a __init__ method that has instance variables - name and age Create instances of class Parrot,
#  passing arguments as well Print Class variable by accessing it Print Instance variables as well
class parrot:
    species="Bird"

    def __init__(self,name,age):
        self.name=name
        self.age=age

blu=parrot("blu",10)
dou=parrot("dou",13)
print("blu is a ",blu.species) 
print("dou is a ",dou.species)       

print(blu.name," is a ",blu.age) 
print(dou.name," is a ",dou.age)       
