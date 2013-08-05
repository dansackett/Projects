"""
Prime Factorization
- Have the user enter a number and find all Prime Factors (if there are any)
and display them.

Call By
- python prime_factorization.py

"""


def pf():
    number = int(raw_input('Enter a number to see its prime factors: '))

    factors = [n for n in range(1, number + 1) if number % n == 0]
    if len(factors) > 2:
        print "{} is not prime!".format(number)
        print "Its factors are: {}".format(', '.join([str(n) for n in factors]))
    else:
        print "{} is prime!".format(number)


if __name__ == '__main__':
    pf()
