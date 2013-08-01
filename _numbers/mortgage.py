"""
Mortgage Calculator
- Calculate the monthly payments of a fixed term mortgage over given Nth terms
at a given interest rate. Also figure out how long it will take the user
to pay back the loan.

I used the equation:
- M = P[i(1+i)^n]/[(1+i)^n -1]
- The monthly payment is M
- The principal (amount of the loan) is P
- The interest rate is i
- The number of payments to make is n.

NOTE:
- Not sure how to compute how long it will take since I still have a hard time
understanding how this calculation works. Not a finance guy.

Call By
- python
- from numbers.mortgage import mortgage
- mortgage()

"""


def mortgage():
    principal = int(raw_input('How much is the mortgage total?: $'))
    interest = int(raw_input('How much is the annual interest rate?: %'))
    term = int(raw_input('How many years is the term?: '))

    monthly_interest = (interest / 100.0) / 12.0
    num_payments = term * 12.0
    term_rate = (1 + monthly_interest) ** num_payments

    monthly_payment = principal * ((monthly_interest * term_rate) / (term_rate - 1))

    print 'You will pay ${0:.2f} per month.'.format(monthly_payment)
