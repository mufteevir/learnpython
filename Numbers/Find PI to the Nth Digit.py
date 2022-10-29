from decimal import *


def chudnovsky(n):
    """
    Get the value of Pi to n number of decimal places by Chudnovsky Algorithm
    :param n:
    :return:
    """
    pi = Decimal(13591409)
    ak = Decimal(1)
    k = 1
    while k < n:
        ak *= -Decimal((6 * k - 5) * (2 * k - 1) * (6 * k - 1)) / Decimal(k * k * k * 26680 * 640320 * 640320)

        val = ak * (13591409 + 545140134 * k)

        d = Decimal((6 * k - 5) * (2 * k - 1) * (6 * k - 1)) / Decimal(k * k * k * 26680 * 640320 * 640320)

        pi += val
        k += 1
    pi = pi * Decimal(10005).sqrt() / 4270934400
    pi = pi ** (-1)
    return pi


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
    my_pi = chudnovsky(N / 14)
    print("Pi = {}".format(str(my_pi)))
