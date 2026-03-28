n = int(input("Enter a number: "))

if n == 0:
    print("No set bit")
else:
    rightmost = n & -n
    print("Rightmost set bit value:", rightmost)