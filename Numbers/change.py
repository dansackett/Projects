"""
Change Return Program
- The user enters a cost and then the amount of money given.
The program will figure out the change and the number of quarters,
dimes, nickels, pennies needed for the change.

- NOTE: There is an odd bug where it is a penny off such that:
    cost = 49.99
    given = 51.00

    1 dollar is given. Not sure what is wrong.

Call By
- python change.py

"""


def change(cost, given):
    if given > cost:
        change = given - cost
        change_list = make_change(change)

        print '\nYour change is ${0:.2f}'.format(change)
        print '\nHere is:'

        for item in change_list:
            print item

    else:
        print 'That won\'t cover the cost!'


def make_change(change):
    change_dict = {price: 0 for price in ['1.00', '.25', '.10', '.05', '.01']}
    change_list = sorted(change_dict, reverse=True)

    for amount in change_list:
        while True:
            new_change = change - float(amount)
            if new_change >= 0:
                change = new_change
                change_dict[amount] += 1
            else:
                break

    language = {
        '1.00': 'dollar',
        '.25': 'quarter',
        '.10': 'dime',
        '.05': 'nickel',
        '.01': 'penny',
    }

    formatted_change = ['{} {}'.format(amount, language[key] + 's')
                        if amount > 1 else '{} {}'.format(amount, language[key])
                        for key, amount in change_dict.items() if amount]

    return formatted_change


if __name__ == '__main__':
    cost = float(raw_input('What is the cost?: $'))
    given = float(raw_input('How much are you paying?: $'))

    change(cost, given)
