# ReverseBits
# Outline:
# Write a Program to reverse all bits present in a number and print a newly formed number.
def reverse_bits(n):
    # Convert to binary (remove '0b')
    binary = bin(n)[2:]
    
    # Reverse the binary string
    reversed_binary = binary[::-1]
    
    # Convert back to decimal
    return int(reversed_binary, 2)

# Input
num = int(input("Enter a number: "))

# Output
result = reverse_bits(num)
print("Reversed bit number:", result)