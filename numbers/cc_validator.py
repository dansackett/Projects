"""
Credit Card Validator
- Takes in a credit card number from a common credit card vendor
(Visa, MasterCard, American Express, Discoverer) and validates it to make sure
that it is a valid number (look into how credit cards use a checksum).

- I've used the Luhn Formula which is:
    - Take the CC number and double every other number starting with the second
    from the right
    - Add double digits together
    - Add the numbers and check that the last digit is zero. If not, it's not
    valid.

Call By
- python
- from numbers.cc_validator import validate
- validate()

"""


def cc_validator():
    cc_num = raw_input('Enter your credit card number to validate: ')

    # I add 0 to the front of the cc number to give it 17 digits making the
    # doubling work correctly from the back
    doubled = [int(x) if i % 2 == 0 else int(x) + int(x)
               for i, x in enumerate('0' + cc_num)]

    doubled_added = [int(str(x)[0]) + int(str(x)[1]) if x >= 10 else x
                     for x in doubled]

    total = sum(doubled_added)

    if total % 10 == 0:
        print 'This card is valid!'
    else:
        print 'This card is not valid!'
