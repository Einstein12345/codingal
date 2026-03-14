# Program to find HCF/GCD
# GCD means greater common divisor
# Enter 2 numbers
numberLargest = int(input("Enter Largest number : "))
numberSmallest = int(input("Enter Smallest number : "))
  
# Using Eucliden Algorithms  
while(numberSmallest):
  numberStore = numberSmallest
  numberSmallest = numberLargest % numberSmallest
  numberLargest = numberStore
 
print("HCF is : ",numberLargest)