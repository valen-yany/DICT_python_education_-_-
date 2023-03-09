import math
import argparse


def main_menu():
    parser = argparse.ArgumentParser()
    parser.add_argument("--type", help="type", )
    parser.add_argument("--principal", help="principal", type=int)
    parser.add_argument("--periods", help="periods", type=int)
    parser.add_argument("--interest", help="interest", type=float)
    parser.add_argument("--payment", help="payment", type=float)
    args = parser.parse_args()
    credit_type = args.type
    principal = args.principal
    periods = args.periods
    interest = args.interest
    payment = args.payment
    if credit_type != 'annuity' and credit_type != 'diff':
        print('Incorrect parameters')
    elif interest is None:
        print('Incorrect parameters')
    elif credit_type == 'diff' and payment is not None:
        print('Incorrect parameters')
    elif credit_type == 'diff' and None in [periods, principal]:
        print('Incorrect parameters')
    elif credit_type == 'annuity' and [periods, principal, payment].count(None) > 1:
        print('Incorrect parameters')
    elif credit_type == 'diff' and False in [periods >= 1, principal >= 1, interest >= 0]:
        print('Incorrect parameters')
    elif credit_type == 'diff':
        get_diff_payment(periods, principal, interest=get_nominal_interest(interest))
    elif credit_type == 'annuity':
        if periods is None and False not in [payment > 0, principal >= 1, interest >= 0]:
            periods = get_periods(principal, payment, interest=get_nominal_interest(interest))
        elif payment is None and False not in [periods >= 1, principal >= 1, interest >= 0]:
            payment = get_payment(periods, principal, interest=get_nominal_interest(interest))
        elif principal is None and False not in [periods >= 1, payment > 0, interest >= 0]:
            principal = get_principal(payment, periods, interest=get_nominal_interest(interest))
        else:
            print('Incorrect parameters')
        overpayment = get_annuity_overpayment(payment, periods, principal)
        print(f'Overpayment = {overpayment}')


def get_nominal_interest(interest):
    return interest / 1200


def get_periods(principal, payment, interest):
    periods = math.ceil(math.log(payment / (payment - interest * principal), 1 + interest))
    years = f'{periods // 12} year{"s" * bool(periods // 12 - 1)}' * bool(periods // 12)
    months = f'{periods % 12} month{"s" * bool(periods % 12 - 1)}' * bool(periods % 12)
    print(f'It will takes {years}{" and " * int(bool(months) and bool(years))}{months} to repay this loan!')
    return periods


def get_payment(periods, principal, interest):
    payment = math.ceil(principal * ((interest * (1 + interest) ** periods) / ((1 + interest) ** periods - 1)))
    print(f'Your monthly payment = {payment}!')
    return payment


def get_principal(payment, periods, interest):
    principal = int(payment / ((interest * (1 + interest) ** periods) / ((1 + interest) ** periods - 1)))
    print(f'Your loan principal = {principal}!')
    return principal


def get_diff_payment(periods, principal, interest):
    months = [math.ceil(principal / periods + interest * (principal - (principal * (i - 1) / periods)))
              for i in range(1, periods + 1)]
    overpayment = 0
    for month, payment in enumerate(months):
        print(f'Month {month + 1}: payment is {payment}!')
        overpayment += payment
    print(f'Overpayment {overpayment - principal}')


def get_annuity_overpayment(payment, periods, principal):
    return math.ceil(payment) * math.ceil(periods) - principal


main_menu()
