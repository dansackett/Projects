"""
Fibonacci Sequence
- Enter a number and have the program generate the Fibonacci sequence
to that number or to the Nth number.

Call By
- python
- from numbers.fib import fib
- fib()

"""


def fib():
    length = int(raw_input('How many numbers of the fibonacci sequence would you like to see?: '))
    numbers = []

    while len(numbers) < length:
        nums_len = len(numbers)
        if nums_len == 1:
            numbers.append(1)
        elif nums_len > 1:
            numbers.append((numbers[-1]) + (numbers[-2]))
        else:
            numbers.append(0)

    print ', '.join([str(n) for n in numbers])
