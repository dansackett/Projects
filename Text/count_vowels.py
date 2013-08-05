"""
Count Vowels
- Enter a string and the program counts the number of vowels in the text.
For added complexity have it report a sum of each vowel found.

Call By
- python count_vowels.py

"""


def count_vowels():
    string = raw_input('Enter a string to count the vowels from: ')
    vowels_dict = {vowel: 0 for vowel in ['a', 'e', 'i', 'o', 'u']}
    for letter in string:
        if letter in vowels_dict.keys():
            vowels_dict[letter] += 1

    for vowel, count in vowels_dict.items():
        if count:
            print '{} appeared {} times.'.format(vowel, count)


if __name__ == '__main__':
    count_vowels()
