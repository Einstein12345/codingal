file =open('outerFile1.txt', 'r')
print("file in read mode")
print(file.read())
file.close()

file =open('outerFile1.txt', 'w')
print("file in write mode")
print(file.write("i am Einstein. "))
file.close()

file =open('outerFile1.txt', 'a')
print("file in Append mode")
print(file.write("i am 11 years old"))
file.close()