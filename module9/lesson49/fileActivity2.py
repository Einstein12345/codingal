file=open("module9/lesson49/file1.txt",'r')
print(file.read())
file.close()

fileWrite=open("module9/lesson49/file1.txt",'w')
fileWrite.write("this is codingal. ")
fileWrite.close()

fileAppend=open("module9/lesson49/file1.txt",'a')
fileAppend.write("Hi i am Einstein")
fileAppend.close()