"""
#Start with a number n > 1. Find the number of steps it takes to reach one using the following process:
#If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.
"""
n = int(input('number is '))
i = 0
while n != 1:
    if n % 2 == 0:
        n = n / 2
    else:
        n = n * 3 + 1
    i += 1

print(f'number of steps {i}')
