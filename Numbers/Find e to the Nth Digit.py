from decimal import *
from math import factorial


def find_e(n):
    """
    Get the value of e to n number of decimal places
    :param n:
    :return:
    """
    e = Decimal(0)
    k = 0
    while k < n+1:
        val = Decimal(1/factorial(k))
        e += val
        k += 1
    return e


def input_number():
    """
    Ask the user for size of fibo
    :return:n
    """
    while True:
        try:
            n = int(input('Please enter a number of digits:'))
        except:
            print('sorry, n must be int')
        else:
            break
    return n


if __name__ == "__main__":
    N = input_number()

    getcontext().prec = N
    my_e = find_e(N)
    print("e = {}".format(str(my_e)))
