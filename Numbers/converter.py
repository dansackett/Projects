"""
Unit Converter (temp, currency, volume, mass and more)
- Converts various units between one another. The user enters the type of
unit being entered, the type of unit they want to convert to and then the
value. The program will then make the conversion.

TODO: More Conversions
- Add volume and mass conversions

Call By
- python converter.py

"""


def converter():
    conversions = {
        't': 'Temperature',
        'c': 'Currency',
        # 'v': 'Volume',
        # 'm': 'Mass',
    }

    print 'Let\'s convert some measurements!\n'
    for letter, measurement in conversions.items():
        print '{}. {}'.format(letter.upper(), measurement)

    conversion_choice = raw_input('\nChoose the letter for the measurement you would like to convert: ').lower()

    if conversion_choice not in conversions.keys():
        print 'Please choose one of the supplied numbers.'

    if conversion_choice == 't':
        convert_temp()
    elif conversion_choice == 'c':
        convert_currency()
    # elif conversion_choice == 'v':
    #     convert_volume()
    # elif conversion_choice == 'm':
    #     convert_mass()


def convert_temp():
    degree = int(raw_input('What is the number of degrees?: '))
    unit1 = raw_input('What unit is that in? (K = Kelvin, C = Celcius, F = Farenheit): ').lower()
    unit2 = raw_input('What unit would you like to convert it to? (K = Kelvin, C = Celcius, F = Farenheit): ').lower()

    formulas = {
        'kc': lambda k: k - 273.15,
        'kf': lambda k: 1.8 * (k - 273.15) + 32,
        'ck': lambda c: c + 273.15,
        'cf': lambda c: ((c * 9) / 5) + 32,
        'fk': lambda f: ((f - 32) * 1.8) + 273.15,
        'fc': lambda f: ((f - 32) * 5) / 9,
    }

    language = {
        'c': 'celsius',
        'f': 'farenheit',
        'k': 'kelvin',
    }

    try:
        result = formulas[unit1 + unit2](degree)
        print '{} degrees {} is {} degrees {}'.format(degree, language[unit1],
                                                      result, language[unit2])
    except KeyError:
        print 'That\'s not a valid conversion.'


def convert_currency():
    language = {
        'd': 'dollars',
        'e': 'euros',
        'y': 'japanese yen',
        'f': 'swiss francs',
        'p': 'mexican pesos',
    }

    amount = float(raw_input('What is the number amount of money?: '))

    print '\nUse one of the following letters to denote the currency:'
    for letter, word in language.items():
        print '{} - {}'.format(letter, word)

    currency1 = raw_input('\nWhat currency is that in?: ').lower()
    currency2 = raw_input('What currency would you like to convert it to?: ').lower()

    # Formulas are current as of August 2, 2013
    formulas = {
        # Dollars
        'de': lambda d: d * 0.75,
        'dy': lambda d: d * 99.81,
        'dp': lambda d: d * 12.85,
        'df': lambda d: d * 0.94,
        # Euros
        'ed': lambda e: e * 1.32,
        'ey': lambda e: e * 131.57,
        'ep': lambda e: e * 16.86,
        'ef': lambda e: e * 1.24,
        # Yen
        'yd': lambda y: y * 0.010,
        'ye': lambda y: y * 0.0076,
        'yp': lambda y: y * 0.13,
        'yf': lambda y: y * 0.0094,
        # Francs
        'fd': lambda f: f * 1.07,
        'fe': lambda f: f * 0.81,
        'fp': lambda f: f * 13.66,
        'fy': lambda f: f * 106.44,
        # Pesos
        'pd': lambda p: p * 0.079,
        'pe': lambda p: p * 0.059,
        'pf': lambda p: p * 0.073,
        'py': lambda p: p * 7.80,
    }

    try:
        result = formulas[currency1 + currency2](amount)
        print '{} {} is {} {}'.format(amount, language[currency1],
                                      result, language[currency2])
    except KeyError:
        print 'That\'s not a valid conversion.'


def convert_volume():
    pass


def convert_mass():
    pass


if __name__ == '__main__':
    converter()
