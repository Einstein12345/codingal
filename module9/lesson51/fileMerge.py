with open('outerFile1.txt') as file1:
    data1=file1.read()
with open('outerFile2.txt') as file2:
    data2=file2.read()
data1+="\n"
data1+=data2
with open('mergedfile.txt','w') as file:
    file.write(data1)