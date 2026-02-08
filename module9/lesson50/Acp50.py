# File Handling Operations – Reading a File in Different Ways

# Make sure "students.txt" exists in the same folder as this program

print("---- Reading entire file using read() ----")
file = open('student.txt', 'r')
content = file.read()
print(content)
file.close()

print("\n---- Reading first line using readline() ----")
file = open("student.txt", "r")
line = file.readline()
print(line)
file.close()

print("\n---- Reading all lines using readlines() ----")
file = open("student.txt", "r")
lines = file.readlines()
for line in lines:
    print(line)
file.close()

print("\n---- Reading file using for loop ----")
file = open("student.txt", "r")
for line in file:
    print(line)
file.close()

print("\n---- Reading file using with statement ----")
with open("student.txt", "r") as file:
    content = file.read()
    print(content)