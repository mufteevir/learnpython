"""
The user enters a cost and then the amount of money given.
The program will figure out the change and the number of quarters, dimes, nickels, pennies needed for the change
the penny is worth 1 cent
the nickel is worth 5 cent
the dime is worth 10 cent
the quarter is worth 25 cent
"""
coins = [['dollar', 'dollars', 100], ['quarter', 'quarters', 25], ['dime', 'dimes', 10], ['nickel', 'nickels', 5],
         ['penny', 'pennies', 1]]


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


def return_find(ch):
    my_str = 'change is '
    for name, name_pl, value in coins:
        n_coins, ch = divmod(ch, value)
        if n_coins > 0:
            if n_coins == 1:
                my_str += '1 ' + name + " "
            else:
                my_str += str(n_coins) + " " + name_pl + " "
    return (my_str)


def main():
    cost = int_input_number("cost is: ")
    given = int_input_number("given money is: ")
    change = given - cost
    print(return_find(change))

if __name__ == '__main__':
    main()
