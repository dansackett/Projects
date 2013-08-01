"""
Calculator
- A simple calculator to do basic operators.
Make it a scientific calculator for added complexity.

Call By
- python
- from _numbers.calc import calc
- calc()

"""


def calc():
    print 'Welcome to the calculator!'

    operation = raw_input('What operation would you like to perform? (+, -, *, /, ^2): ')

    if operation == '^2':
        number = int(raw_input('Enter a number to square: '))
        print '{} squared is {}'.format(number, number ** 2)
    elif operation in ['+', '-', '*', '/']:
        number1 = int(raw_input('Enter the first number: '))
        number2 = int(raw_input('Enter the second number: '))

        if operation == '+':
            print 'The sum is {}'.format(number1 + number2)
        elif operation == '-':
            print 'The difference is {}'.format(number1 - number2)
        elif operation == '*':
            print 'The product is {}'.format(number1 * number2)
        elif operation == '/':
            print 'The quotient is {}'.format(number1 / number2)
    else:
        print 'I\'m sorry, we don\'t support that operation'
