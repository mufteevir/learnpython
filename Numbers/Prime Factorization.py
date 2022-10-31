"""
Python program to print prime factors
"""
from math import sqrt


def end_prime(go):
    """
    ask user to find next number
    :param go:
    :return: go
    """
    while True:
        restart = input("Do you want to type new number? 'y' or 'n':")
        if restart.lower() == 'y':
            go = True
            break
        elif restart.lower() == 'n':
            go = False
            break
        else:
            print("Please type 'y' or 'n'")
            continue
    return go


def prime_factor(n):
    """
    A function to make list of all prime factors of a given number n
    :param n:
    :param lst:
    :return:
    """
    lst = []
    while n % 2 == 0:
        lst.append(2)
        n = n / 2
    for i in range(3, int(sqrt(n) + 1), 2):
        while n % i == 0:
            lst.append(i)
            n = n / i
    if n > 2:
        lst.append(int(n))
    return lst


def input_number():
    """
    Ask the user for number
    :return:n
    """
    while True:
        try:
            n = int(input('Please enter a number to find prime factors:'))
        except:
            print('sorry, n must be int')
        else:
            break
    return n


def main():
    go = True
    while go:
        number = input_number()
        print(prime_factor(number))
        go = end_prime(go)


if __name__ == '__main__':
    main()
