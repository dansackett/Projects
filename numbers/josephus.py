"""
Josephus Problem
- In computer science and mathematics, the Josephus Problem
(or Josephus permutation) is a theoretical problem related to a certain
counting-out game.

There are people standing in a circle waiting to be executed.
The counting out begins at some point in the circle and proceeds around the
circle in a fixed direction. In each step, a certain number of people are
skipped and the next person is executed. The elimination proceeds around
the circle (which is becoming smaller and smaller as the executed people
are removed), until only the last person remains, who is given freedom.

- In my version you input the number of people and amount of skips.
- The first person counts starting with the second person.
- Once you reach the number of people to skip, that person is executed.
- The person who comes after the executed person then starts another count.
- This continues until only one person remains.

Call By
- python
- from numbers.josephus import jospehus
- josephus()

"""


def josephus():
    # I add one to work with indices correctly
    num_people = int(raw_input('How many people are in the circle?: ')) + 1
    skips = int(raw_input('How many skips will there be?: ')) + 1

    people = range(1, num_people)

    execute(people, skips)


# The recursive function for eliminating people and remaking the list
def execute(people, skips):
    print people

    index = reduce_people(len(people), skips)
    people.pop(index)
    people = people[index:] + people[:index]
    if len(people) > 1:
        execute(people, skips)
    else:
        print 'The last one standing is {}!'.format(people[0])


# Returns the correct index for the elimination target
def reduce_people(num_people, skips):
    while True:
        if num_people >= skips:
            return skips - 1
        else:
            skips = skips - num_people
