"""
Binary to Decimal and Back Converter
- Develop a converter to convert a decimal number to binary or a binary number
to its decimal equivalent.

Call By
- python bin_dec.py

"""


def converter(conv_type):
    if conv_type.lower() == 'b':
        binary = raw_input('Enter a binary number: ')

        power_tree = [2 ** x for x in range(0, len(binary))][::-1]

        decimal = sum([num if int(binary[i]) else 0
                       for i, num in enumerate(power_tree)])

        print 'The decimal equivalent is {}.'.format(decimal)

    elif conv_type.lower() == 'd':
        decimal = raw_input('Enter a decimal number: ')

        binary = []
        while True:
            if int(decimal) == 0:
                break
            elif int(decimal) / 2 >= 0:
                binary.append(int(decimal) % 2)
                decimal = int(decimal) / 2
            else:
                break

        binary_eq = ''.join(str(num) for num in binary[::-1])

        print 'The binary equivalent is {}.'.format(binary_eq)

    else:
        print 'Enter either "b" for binary to decimal or "d" for decimal to binary.'


if __name__ == '__main__':
    conv_type = raw_input('Would you like to convert a binary number or decimal number? (b/d): ')

    converter(conv_type)
