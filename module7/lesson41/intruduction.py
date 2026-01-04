Greetings = "hello"
name=input("enter your name?")
age= input("enter your age:")
standard=input("wich class do you go in ?")
school=input("wich school do you attend?")

def intro():       #function defination
    print(Greetings + name)
    print("i am ",age,"years old")
    print("i study in",school,"in class ",standard)

intro()      #