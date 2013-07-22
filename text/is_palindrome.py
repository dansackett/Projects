"""
Check if Palindrome
- Checks if the string entered by the user is a palindrome.
That is that it reads the same forwards as backwards like "racecar"

Call By
- python
- from text.is_palindrome import is_palindrome
- is_palindrome('STRING')

"""


def is_palindrome(string):
    reverse = string[::-1]
    if string == reverse:
        print '{} is a palindrome!'.format(string)
    else:
        print '{} is not a palindrome.'.format(string)
