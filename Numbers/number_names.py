"""
Number Names
- Show how to spell out a number in English.
You can use a preexisting implementation or roll your own, but you should
support inputs up to at least one million (or the maximum value of your
language's default bounded integer type, if that's less). Optional:
Support for inputs other than positive integers (like zero, negative
integers, and floating-point numbers).

Call By
- python
- from _numbers.number_names import number_names
- number_names()

"""

uniques = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five',
           '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine', '10': 'ten',
           '11': 'eleven', '12': 'twelve', '13': 'thirteen', '20': 'twenty',
           '30': 'thirty', '40': 'forty', '50': 'fifty', '60': 'sixty',
           '70': 'seventy', '80': 'eighty', '90': 'ninety'}


def number_names():
    number = raw_input('Enter a number, I\'ll tell you how to say it: ')

    if number in uniques.keys():
        word = uniques[number]
    else:
        # Formulas keyed by length of number
        formulas = {
            '2': lambda number: create_tens(number),
            '3': lambda number: create_hundreds(number),
            '4': lambda number: create_thousands(number),
            '5': lambda number: create_ten_thousands(number),
            '6': lambda number: create_hundred_thousands(number),
            '7': lambda number: create_millions(number),
        }
        word = formulas[str(len(number))](number)

    print '{} is said like "{}".'.format(number, word)


def create_tens(number):
    first = number[0]
    last = number[1]

    # Basic ten
    if last == '0':
        return uniques[number]
    # Single number
    elif first == '0':
        return uniques[last]
    # In the -teen range
    elif first == '1':
        return uniques[last] + 'teen'
    else:
        return uniques[first + '0'] + '-' + uniques[last]


def create_hundreds(number):
    first = number[0]
    last = number[1:]

    # Basic hundred
    if last == '00':
        return uniques[first] + ' hundred'
    # Is a tens number
    elif first == '0':
        return create_tens(last)
    else:
        return uniques[first] + ' hundred and ' + create_tens(last)


def create_thousands(number):
    first = number[0]
    last = number[1:]

    # Basic thousand
    if last == '000':
        return uniques[first] + ' thousand'
    # Is a hundreds number
    elif first == '0':
        return create_hundreds(last)
    else:
        return uniques[first] + ' thousand ' + create_hundreds(last)


def create_ten_thousands(number):
    first = number[:2]
    last = number[2:]

    # Basic ten thousand
    if last == '000':
        return uniques[first] + ' thousand'
    # Is a thousands number
    elif first == '00':
        return create_thousands(last)
    # Has unique start
    elif first in uniques.keys():
        return uniques[first] + ' thousand ' + create_hundreds(last)
    else:
        return create_tens(first) + ' thousand ' + create_hundreds(last)


def create_hundred_thousands(number):
    first = number[:3]
    last = number[3:]

    # Basic hundred thousand
    if last == '000':
        return create_hundreds(first) + ' thousand'
    # Is a ten thousands
    elif first == '000':
        return create_ten_thousands(last)
    else:
        return create_hundreds(first) + ' thousand ' + create_hundreds(last)


def create_millions(number):
    first = number[0]
    last = number[1:]

    # Basic Million
    if last == '000000':
        return uniques[first] + ' million'
    else:
        return uniques[first] + ' million ' + create_hundred_thousands(last)
