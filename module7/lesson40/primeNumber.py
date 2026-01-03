num=int(input("enter the number to be checked"))
flag=False

if num>1:
    for i in range(2,num):
        if (num%i)==0:
            flag=True
            break
if flag:      #it will check if flag is true
    print(num," is not a prime number")
else:
    print(num," is a prime number")        