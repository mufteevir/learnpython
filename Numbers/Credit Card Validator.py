"""
Takes in a credit card number from a common credit card vendor
and validates it to make sure that it is a valid number (look into how credit cards use a checksum).
Using Luhn algorithms and MOD 10 checksums

Calculating the Luhn algorithm by hand includes a few different steps. They include the following.
      1. Write down the credit card number:
4417 1234 5678 9113
      2. Starting from the first number, double every other digit.
4(x2) 4 1(x2) 7 1(x2) 2 3(x2) 4 5(x2) 6 7(x2) 8 9(x2) 1 1(x2) 3
The doubled numbers result in: 8 2 2 6 10 14 18 2
        3. If the result of the doubling ends up with a two digits, then add those two digits together:
10 = 1+0 14= 1+4 18= 1+8
        4. Add up all numbers: 8+4+2+7 + 2+2+6+4 + 1+0+6+1+4+8 + 1+8+1+2+3 = 70

If the final sum is divisible by 10, then the credit card is valid.
If it is not divisible by 10, the number is invalid or fake.
In the above example, credit card number 4417 1234 5678 9113 has passed the Luhn test.
"""


def number_to_arr(n):
    number_arr = []
    for i in n:
        number_arr.append(i)
    return number_arr


def number_transform(number_arr):
    for i in range(0, len(number_arr), 2):
        digit = int(number_arr[i]) * 2
        if digit < 10:
            number_arr[i] = digit
        else:
            number_arr[i] = digit // 10 + digit % 10
    return number_arr


def check_sum(number_arr):
    sum = 0
    for i in range(0, len(number_arr)):
        sum += int(number_arr[i])
    if sum % 10 == 0:
        print('True')
    else:
        print('False')
    print(f'Checksum is {sum}')


def main():
    credit_card_number = input('Enter CC number to validate\r\n>')
    number_arr = number_transform(number_to_arr(credit_card_number))
    check_sum(number_arr)


main()
