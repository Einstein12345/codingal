#Longest1’s
#Outline:
# Write a Program to find the longest consecutive 1’s in the binary representation of a number.
def longest_consecutive_ones(n):
    binary = bin(n)[2:]  # convert to binary and remove '0b'
    
    max_count = 0
    current_count = 0
    
    for bit in binary:
        if bit == '1':
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0
    
    return max_count


# Example usage
num = int(input("Enter a number: "))
result = longest_consecutive_ones(num)

print("Binary:", bin(num)[2:])
print("Longest consecutive 1's:", result)