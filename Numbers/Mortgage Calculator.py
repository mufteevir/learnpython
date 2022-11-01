"""**Mortgage Calculator** -
Calculate the monthly payments of a fixed term mortgage
over given Nth terms at a given interest rate. Also figure
out how long it will take the user to pay back the loan."""
import calendar
import datetime


def add_months(sourcedate, months):
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month // 12
    month = month % 12 + 1
    day = min(sourcedate.day, calendar.monthrange(year, month)[1])
    return datetime.date(year, month, day)


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


def main():
    months = int_input_number("Enter mortgage term (in months): ")
    rate = int_input_number("Enter interest rate: ")
    loan = int_input_number("Enter loan value: ")

    today = datetime.date.today()
    till_data = add_months(today, months - 1)

    print(f'data of calculations is {today}')

    monthly_rate = rate / 100 / 12
    payment = loan * (monthly_rate + monthly_rate / (((1 + monthly_rate) ** months) - 1))

    print(f'for loan {loan:6.1f} and interest rate {rate} monthly payment is {payment: 5.1f} till {till_data}')

    debt_part = loan * monthly_rate
    till_data = today

    while loan > payment:
        print(
            f'{till_data} for loan {loan: 6.1f} | monthly payment is {payment: 5.1f} | debt part is {debt_part: 5.1f}')
        loan = loan - (payment - debt_part)
        debt_part = loan * monthly_rate
        till_data = add_months(till_data, 1)
    else:
        debt_part = 0
        print(f'{till_data} for loan {loan: 6.1f} | monthly payment is {loan: 5.1f} | debt part is {debt_part: 5.1f}')


if __name__ == '__main__':
    main()
