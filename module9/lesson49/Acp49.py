# Read a file
with open("file1.txt","r") as f:
    text = f.read()

# Create or overwrite a file
with open("log.txt", "w") as f:
    f.write("Log started\n")

# Append to a file
with open("log.txt", "a") as f:
    f.write("New entry\n")