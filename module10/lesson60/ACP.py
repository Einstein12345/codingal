# 2digitPrimes
# Outline:
# Write a program to find all the prime numbers having 2 digits.
def is_prime(n):
    """Checks if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Find and print all 2-digit prime numbers
two_digit_primes = []
for num in range(10, 100):
    if is_prime(num):
        two_digit_primes.append(num)

print("2-Digit Prime Numbers:")
print(two_digit_primes)
print(f"\nTotal count: {len(two_digit_primes)}")