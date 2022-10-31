"""
Calculate the total cost of tile it would take to cover a floor plan of width and height,
using a cost entered by the user.
"""


def int_input_number(str):
    """
    Ask the user for number
    :return:n
    """
    while True:
        try:
            n = int(input(str))
        except:
            print('sorry, n must be int')
        else:
            break
    return n


def float_input_number(str):
    """
    Ask the user for number
    :return:n
    """
    while True:
        try:
            n = float(input(str))
        except:
            print('sorry, n must be float')
        else:
            break
    return n


def main():
    W = float_input_number("Width of floor: ")
    H = float_input_number("Length of floor: ")
    C = float_input_number("Cost of Tile: ")
    print(f'total cost of tile is {W * H * C : 10.4f}')


if __name__ == '__main__':
    main()
