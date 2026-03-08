# Calculate the time complexity of the recursive function.
# here the recursion function will take 2 recursive calls and rest of the code will take a constant time.
def myFunc(n):          #function definition
    if n<=0:
        return
    print("codingal") #Constant extra work
    myFunc(n//2)#recursive call1
    myFunc(n//2)#recursive call2
myFunc(8)
#recurence relations will be
# T(n)=T(n/2)+T(n/2)+ O(1)    ie. O(1) as constant time.
# Two recursive calls and a Constant extra work
# time complexity is =O(n)