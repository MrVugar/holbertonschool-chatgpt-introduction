#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given number using recursion.

    Parameters:
        n (int): The number to calculate the factorial for. Must be a non-negative integer.

    Returns:
        int: The factorial of the number. Returns 1 if n is 0.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Calculate and print the factorial of the number passed as a command-line argument
f = factorial(int(sys.argv[1]))
print(f)
