def power8(number):
    
    # As the power of 2 will have only 1 set bit, then n-1 & n will always be 0 for any power of 2
    if (number == 0):
        return 0
    if ((number & (~(number - 1))) == number):                                    #~ this the bit wise not11
        return 1
    return 0
  
number = int(input("Enter the number : "))
 
if(power8(number)):
    print("\nThe number is power of 8")
else:
    print("\nThe number is not power of 8")
# time complexity is eqaul to O(1). space complexity is O(1)