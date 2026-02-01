file=open("module9/lesson49/file1.txt",'r')
counter=0

content=file.read()
contentList=content.split("\n")

for i in contentList :
    if i :
        counter+=1
print("number of lines in the file : ",counter)        