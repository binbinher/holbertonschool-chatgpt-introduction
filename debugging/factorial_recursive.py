#!/usr/bin/python3
import sys


def factorial(n):
    """
    Recursive function to calculate the factorial of a number.

    Args:
        n (int): The number for which factorial is to be calculated.

    Returns:
        int: The factorial of the input number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


# Get the input from command line argument and calculate factorial
f = factorial(int(sys.argv[1]))

# Print the result
print(f)