"""
Sieve of Eratosthenes is a method for finding all primes up to (and possibly including) a given natural.
This method works well when is relatively small, allowing us to determine whether any natural number
less than or equal to is prime or composite.
"""
n = int(input('input a number '))
a = []
for i in range(n + 1):
    a.append(i)

a[1] = 0

i = 2
while i <= n:
    if a[i] != 0:
        j = i + i
        while j <= n:
            a[j] = 0
            j = j + i
    i += 1

a = set(a)
a.remove(0)
print(a)
