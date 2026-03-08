# Recurrence Relations
# Outline:
# Print the recurrence relation of the following recursive functions given.
# include <studio.h>
# Recursive function
#include <stdio.h>

#  Recursive function
def f(n):
    if n <= 1:
        return 1
    else:
        return 2 * f(n-1)


n = int(input("Enter value of n: "))


result = f(n)


print("Result:", result)


print("\nRecurrence Relation:")
print("T(n) = T(n-1) + O(1)")


print("\nTime Complexity:")
print("O(n)")


print("\nSpace Complexity:")
print("O(n)")