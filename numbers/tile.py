"""
Find Cost of Tile to Cover W x H Floor
- Calculate the total cost of tile it would take to cover a floor plan
of width and height, using a cost entered by the user.

Call By
- python
- from numbers.tile import tile
- tile()

"""


def tile():
    cost = float(raw_input('What is the cost per square inch of tile?: $'))
    width = float(raw_input('How many square feet wide is the area?: '))
    height = float(raw_input('How many square feet high is the area?: '))

    print 'At ${} per square foot per tile, a {}x{} area would cost ${}'.format(
        cost, int(width), int(height), cost * width * height
    )
