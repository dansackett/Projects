"""
Tax Calculator
- Asks the user to enter a cost and either a country or state tax.
It then returns the tax plus the total cost with tax.

Call By
- python tax_calc.py

"""


def tax_calc():
    print 'Welcome to the tax calculator!'

    cost = float(raw_input('What\'s this thing cost?: $'))
    tax_percent = float(raw_input('What\'s the tax in this place?: %'))

    tax = cost * (tax_percent / 100)

    print '\nRight, so the tax will be ${0:.2f}.'.format(tax)
    print 'The total cost will be ${0:.2f}.'.format(cost + tax)


if __name__ == '__main__':
    tax_calc()
