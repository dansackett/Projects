"""
Check if Palindrome
- Checks if the string entered by the user is a palindrome.
That is that it reads the same forwards as backwards like "racecar"

Call By
- python
- from _text.is_palindrome import is_palindrome
- is_palindrome()

"""


def is_palindrome():
    string = raw_input('Enter a string to check if it\'s a palindrome: ')
    reverse = string[::-1]
    if string == reverse:
        print '{} is a palindrome!'.format(string)
    else:
        print '{} is not a palindrome.'.format(string)
