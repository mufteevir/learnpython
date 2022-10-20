# Fibonacci Sequence Generator
# Have the user enter a number and
# generate a fibonacci sequence
# which size is equivalent to that number.

def fibo(n):
    """
    Generates a fibonacci sequence
    with the size of n
    :param n:
    :return:print(my_list)
    """
    my_list = [0, 1]
    for i in range(2, n):
        my_list.append((my_list[i - 2] + my_list[i - 1]))
    print(my_list)


def input_number():
    """
    Ask the user for size of fibo
    :return:n
    """
    while True:
        try:
            n = int(input('Please enter a number:'))
        except:
            print('sorry, n must be int')
        else:
            break
    return n


def end_fibo(go):
    """
    ask user for try again
    :param go:
    :return: go
    """
    while True:
        restart = input("Do you want try again? 'y' or 'n':")
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


def main():
    go = True
    while go:
        n = input_number()
        fibo(n)
        go = end_fibo(go)


if __name__ == '__main__':
    main()
