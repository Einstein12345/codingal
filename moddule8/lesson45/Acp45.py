#Robot Introduction
#Outline:
#Create a program to introduce your robot using OOPs concepts.
class Robot:
    def __init__(self, name, purpose):
        self.name = name          # Encapsulation
        self.purpose = purpose

    def introduce(self):
        print(f"Hello! I am {self.name}.")
        print(f"My purpose is {self.purpose}.")


# Derived class (Inheritance)
class ServiceRobot(Robot):
    def __init__(self, name, purpose, service_type):
        super().__init__(name, purpose)
        self.service_type = service_type

    # Polymorphism (method overriding)
    def introduce(self):
        print(f"Hello! I am {self.name}, a service robot.")
        print(f"My purpose is {self.purpose}.")
        print(f"I specialize in {self.service_type}.")


# Creating objects
robot1 = Robot("RoboX", "assisting humans")
robot2 = ServiceRobot("HelperBot", "providing services", "healthcare assistance")

# Calling methods
robot1.introduce()
print()
robot2.introduce()
