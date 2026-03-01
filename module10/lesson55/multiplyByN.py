# MultiplyByN
# Outline:
# Write a program to multiply N to M, using 2 functions: 1 iteration and N iterations.
# do analysis
# Function
def multiply_one_iteration(n, m):
    """Multiplies n and m using the built-in operator."""
    return n * m

def multiply_n_iterations(n, m):
    """Multiplies n and m by adding m to the total n times."""
    result = 0
    # Loop runs exactly n times
    for _ in range(abs(n)):
        result += m
    
    # Adjust the sign if n was negative
    return result if n >= 0 else -result

# --- Testing the functions ---
n_value = 6
m_value = 7

print(f"Method 1 (Direct): {multiply_one_iteration(n_value, m_value)}")
print(f"Method 2 ({n_value} iterations): {multiply_n_iterations(n_value, m_value)}")