"""
The factorial of a positive integer *n* is defined as the product of the sequence , n-1, n-2, ...1
and the factorial of 0 is defined as being 1. Solve this using both loops and recursion.
"""

number = 10


# using loops 5!=1*2*3*4*5
def factorial_loops(n):
    factorial = 1
    if n == 0:
        return 1
    else:
        for i in range(1, n + 1):
            factorial *= i
        return factorial


print(factorial_loops(number))


# using recursion
def factorial_recursion(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursion(n - 1)


print(factorial_recursion(number))
