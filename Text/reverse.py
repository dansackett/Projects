"""
Reverse a String
- Enter a string and the program will reverse it and print it out.

Call By
- python reverse.py

"""


def reverse():
    string = raw_input('Enter a string to reverse: ')
    print string[::-1]


if __name__ == '__main__':
    reverse()
