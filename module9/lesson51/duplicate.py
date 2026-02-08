# Write a Python program to duplicate from one file and then copy it to another file. For copying it in a new file,
#  create a new empty file and upload it in a similar way as you do for the given file.
outputfile=open('updatedfile.txt','w')
inputfile=open('repeatedfile.txt','r')

lineseen=set()
for line in inputfile:
    if line not in lineseen:
        outputfile.write(line)
        lineseen.add(line)
inputfile.close()
outputfile.close()        