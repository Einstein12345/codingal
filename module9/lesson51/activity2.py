import os
if os.path.exists("outerFile1.txt"):
    print("the file exist")
else:
    print("the file doesint exsist")

myfile=open("filea.txt","w")
myfile.write("i am Einstein")
myfile.close()

os.remove('filea.txt')



os.rmdir("sample")