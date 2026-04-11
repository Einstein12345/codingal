# Write a Program to find all substrings of a string.w
# Program to print all substrings of a string

def find_substrings(s):
    n = len(s)
    substrings = []

    for i in range(n):
        for j in range(i + 1, n + 1):
            substrings.append(s[i:j])

    return substrings


# Input from user
string = input("Enter a string: ")

result = find_substrings(string)

print("All substrings are:")
for sub in result:
    print(sub)