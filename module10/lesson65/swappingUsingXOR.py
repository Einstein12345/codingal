def swap (a,b):
    a=a^b                  #using the bit wise XOR operator
    b=a^b
    a=a^b
    print("after swapping a=",a,"b=",b)
swap (40,55)