# Check if the given number is an Armstrong number or not.
num=int(input("enter the number"))
digits=len(str(num))         #to find the number of digits 
resultNumber=0                 #initialise variabel
temp=num
while temp > 0:
   digit = temp % 10
   resultNumber += digit ** digits
   temp //= 10
 
# display the result
if num == resultNumber:
   print(num,"is an Armstrong number")
else:
   print(num, "is not an Armstrong number")

# 370
#  3^3 + 7^3 + 0^3 = 370
# 371
#  3^3 + 7^3 + 1^3 = 371
# 407
#  4^3 + 0^3 + 7^3 = 407
# 1634
#  1^4 + 6^4 + 3^4 + 4^4 = 1634
# 8208
#  8^4 + 2^4 + 0^4 + 8^4 = 8208
# 9474
#  9^4 + 4^4 + 7^4 + 4^4 = 9474


