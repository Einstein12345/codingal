firstFile =input("enter first file name ")
secondFile =input("enter second file name ")

f1=open(firstFile,"r")
f2=open(secondFile,"r")

f1.close()
f2.close()

f1=open(firstFile,"a+")
f2=open(secondFile,"r")
f1.write(f2.read())
f1.seek(0)
f2.seek(0)

f1.close()
f2.close()