"""
Next Prime Number
- Have the program find prime numbers until the user chooses to stop asking
for the next one.

Call By
- python
- from _numbers.primes import get_primes
- get_primes()

"""


def get_primes():
    current = 1

    print 'Let\'s generate prime numbers:'
    print current

    while True:
        response = raw_input('Would you like another? (Y/N): ').lower()
        if response == 'y':
            current = next_prime(current)
        elif response == 'n':
            break
        else:
            print 'Invalid response...'


def next_prime(number):
    while True:
        if is_prime(number):
            print number
            return number + 1
        else:
            number += 1


def is_prime(number):
    return len([n for n in range(1, number + 1) if number % n == 0]) == 2
