# Write a Python program to remove lines of a file starting with prefix - Coding and store the contents in a new file.
file1 = open('outerFile1.txt', 'r')
file2 = open('outerFile2.txt', 'w')

for line in file1.readlines():
    if not (line.startswith('Coding')):
        print(line)
        file2.write(line)
file1.close()
file2.close()        