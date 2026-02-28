# OneAlgoThreeFaces
# Outline:
# Calculate the time complexity

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