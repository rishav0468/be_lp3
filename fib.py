
def fib_iterative(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Example usage
# n = int(input("Enter a number for non-recursive Fibonacci: "))
# print(f"Fibonacci number (non-recursive) at position {n} is:", fib_iterative(n))


def fib_recursive(n):
    # Base cases
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    # Recursive calls
    return fib_recursive(n - 1) + fib_recursive(n - 2)

# Example usage
# n = int(input("Enter a number for recursive Fibonacci: "))
# print(f"Fibonacci number (recursive) at position {n} is:", fib_recursive(n))
method = input("Choose method ('iterative' or 'recursive'): ")
n = int(input("Enter a number for Fibonacci: "))

# Calculate Fibonacci based on the chosen method
if method == "iterative":
    result = fib_iterative(n)
elif method == "recursive":
    result = fib_recursive(n)
else:
    result = "Invalid method selected."

print(f"Fibonacci number at position {n} is:", result)


