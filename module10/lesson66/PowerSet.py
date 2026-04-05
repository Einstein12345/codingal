# Write a Program to find the power set of a set.
# a power set is the set of all posible subsets of a set
# eg. set={1,2}
# power set={},{1},{2},{1,2}
# Program to find power set of a set
# Total subsets = 2^n where n is number of elements.
import math;
 
def printPowerSet(set,SetSize):
    
    # Find total elements possible in the power set
    PowerSetSize = (int) (math.pow(2, SetSize));
    outer = 0;
    inner = 0;
    
    for outer in range(0, PowerSetSize):
        for inner in range(0, SetSize):
            # Check if inner bit in the outer is set If set then print inner element from set
            if((outer & (1 << inner)) > 0):
                print(set[inner], end = "")
        print("")
 
size = int(input("Enter array size : "))
 
set = []
for i in range(0,size):
    n = int(input("Enter element : "))
    set.append(n)
 
printPowerSet(set, len(set))
# Time Complexity
# Outer loop → 2^n
# Inner loop → n
# Total: O(n × 2ⁿ)
