#Outline:
# Write a program to create a parent class Person (attributes - name, idnumber) with a method display to display the
#  attributes. Create a child class Employee (attributes - name, idnumber, salary, post). Access the attributes of
#  parent class in child class. Then, create an object for child class and call the display method to display the 
# name and idnumber.
class persson(object):     #parent class 
    def __init__(self,name,idnumber):
        self.name =name
        self.idnumber =idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)

#child class
class employee(persson):
    def __init__(self,name,idnumber,salary,post):
        self.salary =salary
        self.post =post

        persson.__init__(self,name,idnumber)

a=employee("Einstein",211,1000,"junior")
a.display()
