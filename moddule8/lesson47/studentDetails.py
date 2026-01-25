#Write a program to create a parent class Person (attributes - fname, lname) with a method printname to display the
#  full name. Create a child class Student (attributes - fname, lname, year). Access the attributes of parent class 
# in child class using super() function. Then, create an object for the child class and call the display method to
#  display the full name. Also, print the graduation year.
class Person:                      #parent class
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):                 #child class
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)              #supper method is used.invoking the __init__ of  parent class
        self.graduationyear = year
x = Student("Joey", "King", 2021)
x.printname()
print(x.graduationyear)