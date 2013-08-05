"""
Happy Numbers
- A happy number is defined by the following process.
Starting with any positive integer, replace the number by the sum of the
squares of its digits, and repeat the process until the number equals 1
(where it will stay), or it loops endlessly in a cycle which does not include
1. Those numbers for which this process ends in 1 are happy numbers,
while those that do not end in 1 are unhappy numbers.
Display an example of your output here. Find first 8 happy numbers.

Call By
- python happy_numbers.py

"""


def happy():
    number = int(raw_input('How many happy numbers would you like to see?: '))

    # This will yield up to 1000
    if number > 143:
        print 'We only calculate up to 143 numbers'
    else:
        numbers = find_happy_numbers(number)
        print numbers


def find_happy_numbers(number):
    happy_numbers = []

    for num in xrange(1, 1001):
        if is_happy(num):
            if len(happy_numbers) == number:
                return happy_numbers
            else:
                happy_numbers.append(num)


def is_happy(number):
    dig_sum = sum([int(num) ** 2 for num in list(str(number))])
    if dig_sum == 1:
        return True
    # If it is 4 then it is looping
    # http://stackoverflow.com/a/12676003/1639449
    elif dig_sum == 4:
        return False
    elif dig_sum > 1:
        return is_happy(dig_sum)


if __name__ == '__main__':
    happy()
