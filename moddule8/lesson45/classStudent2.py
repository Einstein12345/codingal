#Write a program to create a class with name Student and perform the following tasks - Create a class variable grade and name Create a function to print a sentence Create a function to print class variables grade and name Create an object of class Student Call the two functions to execute them
class student:
    Grade=5   #class variable
    name="Einstein"
    
    def introduction(self):
        print("hi i am a student")
    def details(self):
        print("my name is ",self.name)
        print("i study in ",self.Grade)


ob=student()       #object creation of class student
ob.introduction()
ob.details()