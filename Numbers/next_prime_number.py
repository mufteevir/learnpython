"""
Find the next prime number until the user chooses to stok asking for the next
one
"""
from math import sqrt


def end_prime(go):
    """
    ask user to find next prime number
    :param go:
    :return: go
    """
    while True:
        restart = input("Do you want to find next prime? 'y' or 'n':")
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


def if_prime(n, lst):
    """
    check number for is prime or not. Looking only for dividers not more sqrt of number and only in list of prime numbers
    :param n:
    :param lst:
    :return:
    """
    for j in lst:
        if j > int((sqrt(n)) + 1):
            lst.append(n)
            return True
            break
        if n % j == 0:
            return False
            break
    else:
        lst.append(n)
        return True


def main():
    number = 2
    my_list = []
    go = True
    while go:
        if if_prime(number, my_list):
            print(f'{number} is prime number')
            go = end_prime(go)
        number += 1


if __name__ == '__main__':
    main()
