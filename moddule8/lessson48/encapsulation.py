# Encapsulation Implementation
# Outline:
# Write a program to create a class Computer with a private attribute max_price and methods sell(to display)
#  the selling price and setmaxprice(change the private attribute max_price). Now create an object for the 
# class Computer. Try changing the value of max price and use the sell function to display the updated 
# price. Use a setter function to update the value and again display the price.
class computer:
    def __init__(self):
        self.__maxPrice=900         # __maxprice is the private aattribute
    def sell(self):
        print("selling price is ",self.__maxPrice)
    def setMaxPrice(self,price):      #setter function to change the private attribute max price
        self.__maxPrice=price
c=computer()
c.sell()

c.__maxPrice=1000
c.sell()

c.setMaxPrice(1500)                    #changing max price using setter function
c.sell()