"""
Check if Palindrome
- Checks if the string entered by the user is a palindrome.
That is that it reads the same forwards as backwards like "racecar"

Call By
- python is_palindrome.py

"""


def is_palindrome():
    string = raw_input('Enter a string to check if it\'s a palindrome: ')
    reverse = string[::-1]
    if string == reverse:
        print '{} is a palindrome!'.format(string)
    else:
        print '{} is not a palindrome.'.format(string)


if __name__ == '__main__':
    is_palindrome()
