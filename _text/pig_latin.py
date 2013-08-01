"""
Pig Latin
- Pig Latin is a game of alterations played on the English language game.
The usual rules for changing standard English into Pig Latin are as follows:
For words that begin with consonant sounds, the initial consonant or
consonant cluster is moved to the end of the word, and "ay" is added, as in
the following examples:

"happy" -> "appyhay"
"duck"  -> "uckday"
"glove" -> "oveglay"

For words that begin with vowel sounds or silent letter, "way" is added at
the end of the word. Examples are:

"egg"   -> "eggway"
"inbox" -> "inboxway"
"eight" -> "eightway"

Call By
- python
- from _text.pig_latin import pig_latin
- pig_latin()

"""


def pig_latin():
    string = raw_input('Enter a string to turn into pig latin: ')

    cluster = []
    for letter in string:
        if not is_vowel(letter):
            cluster.append(letter)
        else:
            break

    if len(cluster):
        print string[len(cluster):] + ''.join(cluster) + 'ay'
    else:
        print string + 'way'


def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u']
