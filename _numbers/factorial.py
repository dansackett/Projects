"""
Factorial Finder
- The Factorial of a positive integer, n, is defined as the product of the
sequence n, n-1, n-2, ...1 and the factorial of zero, 0, is defined as being 1.
Solve this using both loops and recursion.

Call By
- python
- from numbers.factorial import factorial
- factorial()

"""


def factorial():
    number = int(raw_input('Enter a positive integer to find its factorial: '))

    # 0
    if number < 0:
        print 'I said POSITIVE integer...'
    elif not number:
        print 'The factorial of 0 equals 1'
    else:
        total = 1
        number_range = range(1, number + 1)
        factorial_string = ' x '.join([str(x) for x in number_range[::-1]])
        for x in number_range:
            total *= x
        print '\n{}! = {}'.format(number, factorial_string)
        print '\nThe factorial of {} equals {}.'.format(number, total)
