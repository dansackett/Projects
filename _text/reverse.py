"""
Reverse a String
- Enter a string and the program will reverse it and print it out.

Call By
- python
- from _text.reverse import reverse
- reverse()

"""


def reverse():
    string = raw_input('Enter a string to reverse: ')
    print string[::-1]
