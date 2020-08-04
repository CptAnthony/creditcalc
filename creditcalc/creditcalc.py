import sys
import math
import argparse


def months_count(principal, payment, interest):
    nominal_rate = interest / 100 / 12
    i = payment / (payment - nominal_rate * principal)
    periods = math.ceil(math.log(i, nominal_rate + 1))
    years_int = periods // 12
    months_int = periods % 12
    overpayment = payment * periods - principal
    if years_int == 0:
        if months_int == 1:
            print(f"You need {months_int} month to repay this credit!")
        else:
            print(f"You need {months_int} months to repay this credit!")
    else:
        if years_int == 1:
            if months_int == 1:
                print(f"You need {years_int} year and {months_int} month to repay this credit!")
            else:
                print(f"You need {years_int} year and {months_int} months to repay this credit!")
        elif months_int == 0:
            print(f"You need {years_int} years to repay this credit.")
        else:
            print(f"You need {years_int} years and {months_int} months to repay this credit.")
    print(f"Overpayment = {overpayment}")


def annuity_payment(principal, periods, interest):
    nominal_rate = interest / 100 / 12
    top = nominal_rate * (1 + nominal_rate) ** periods
    bottom = (1 + nominal_rate) ** periods - 1
    ordinary_annuity = math.ceil(principal * (top / bottom))
    overpayment = ordinary_annuity * periods - principal
    print(f"Your annuity payment = {ordinary_annuity}!")
    print(f"Overpayment = {overpayment}")


def credit_principal(payment, periods, interest):
    nominal_rate = interest / 100 / 12
    bottom_top = nominal_rate * (1 + nominal_rate) ** periods
    bottom_bottom = (1 + nominal_rate) ** periods - 1
    c_principal = int(payment / (bottom_top / bottom_bottom))
    overpayment = payment * periods - c_principal
    print(f"Your credit principal = {c_principal}!")
    print(f"Overpayment = {overpayment}")


def diff_payment(principal, periods, interest):
    total_paid = 0
    nominal_rate = interest / 100 / 12
    for current_period in range(1, periods + 1):
        payment = math.ceil((principal / periods) + nominal_rate *
                            (principal - (principal * (current_period - 1) / periods)))
        total_paid += payment
        print(f"Month {current_period}: paid out {payment}")

    overpayment = total_paid - principal

    print()
    print(f"Overpayment = {overpayment}")


parser = argparse.ArgumentParser()
parser.add_argument('--type', required=False)
parser.add_argument('--principal', type=int, required=False)
parser.add_argument('--interest', type=float, required=False)
parser.add_argument('--payment', type=int, required=False)
parser.add_argument('--periods', type=int, required=False)
args = parser.parse_args()
args_count = vars(args)


if args.type != 'diff' and args.type != 'annuity':
    print("Incorrect parameters")
    sys.exit()

value_counter = 0
for value in args_count.values():
    if value != 'diff' and value != 'annuity':
        if value is None:
            value_counter += 1
    if 1 < value_counter:
        print("Incorrect parameters")
        sys.exit()

if args.type == 'diff':
    if 0 < args.principal and 0 < args.periods and 0 < args.interest:
        diff_payment(args.principal, args.periods, args.interest)
    else:
        print("Incorrect parameters")
elif args.type == 'annuity':
    if args.principal is None:
        if 0 < args.payment and 0 < args.periods and 0 < args.interest:
            credit_principal(args.payment, args.periods, args.interest)
        else:
            print("Incorrect parameters")
    if args.payment is None:
        if 0 < args.principal and 0 < args.periods and 0 < args.interest:
            annuity_payment(args.principal, args.periods, args.interest)
        else:
            print("Incorrect parameters")
    if args.periods is None:
        if 0 < args.principal and 0 < args.payment and 0 < args.interest:
            months_count(args.principal, args.payment, args.interest)
        else:
            print("Incorrect parameters")

