
# Outline:
# Do the basic asymptomatic analysis for the functions written in the previous activity.

# method1 :equation method
def function1(n):
    return n*(n+1)/2
print(function1(4))

# method2 :loop method
def function2(n):
    sum=0
    for i in range(1,n+1):
        sum +=i

# method3 nested loop method()
def function3(n):
    sum=0
    for i in range(1,n+1):
        for j in range(i,i+1):
            sum+=1
        return sum

# analysis
# function1 uses direct formula,so it runs in constant time. O(1)
# function2 uses loop,it runs in linear time.O(n)
# function3 uses neasted loop,it runs in quadratic time O(n square)

# function1is the best and fastest
# function2 is the  medium
# functionn3 is the slowest

# Graph
# Fun1 (O(1)) → flat line (time does not increase with n).
# Fun2 (O(n)) → straight line increasing with n.
# Fun3 (O(n²)) → grows much faster (like a curve upwards).

# Time Complexity = how long an algorithm takes (steps/iterations).
# Examples: O(1), O(log n), O(n), O(n²), etc.
# Space Complexity = how much extra memory it uses.