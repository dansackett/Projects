"""
Count Words in a String
- Counts the number of individual words in a string.
For added complexity read these strings in from a text
file and generate a summary.

Call By
- python
- from _text.count_words import count_words
- count_words('text/test.txt')

"""


def count_words(_file):
    doc = open(_file, 'r')
    text = doc.read()
    counts = {}
    for word in text.split(' '):
        if word in counts.keys():
            counts[word] += 1
        else:
            counts[word] = 1

    for word, count in counts.items():
        print '\'{}\' appeared {} times.'.format(word, count)
