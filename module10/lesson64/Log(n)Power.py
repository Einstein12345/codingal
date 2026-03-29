# Program to computer x^y without using math function
 
 
def computePower( x, y):
 
    # Default total is 1
    result = 1
 
    while (y > 0):
        # If y is even 
        if (y % 2 == 0):
            x = x * x
            y>>=1                        #right shift operator
        
        else:
            result = result * x
            y = y - 1
        
    return result
 
 
x = int(input("Enter x for x^y : "))
y = int(input("Enter y for x^y : "))
print("Total : ",(computePower(x, y)))
# Time Complexity: O(log y)
# Space Complexity: O(1) (constant space)