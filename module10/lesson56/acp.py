# Calculate and print the time complexity of the code snippet below.

def example_O1():
    # Constant time
    x = 10
    y = x * 2
    print("Example 1 Time Complexity: O(1)")


def example_On(n):
    # Single loop
    for i in range(n):
        pass
    print("Example 2 Time Complexity: O(n)")


def example_On2(n):
    # Nested loops
    for i in range(n):
        for j in range(n):
            pass
    print("Example 3 Time Complexity: O(n^2)")


def example_Ologn(n):
    # Logarithmic loop
    i = 1
    while i < n:
        i *= 2
    print("Example 4 Time Complexity: O(log n)")


def example_Onlogn(n):
    # Combination
    for i in range(n):
        j = 1
        while j < n:
            j *= 2
    print("Example 5 Time Complexity: O(n log n)")


# Run examples
n = 10
example_O1()
example_On(n)
example_On2(n)
example_Ologn(n)
example_Onlogn(n)