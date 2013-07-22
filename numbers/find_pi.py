"""
Find PI to the Nth Digit
- Enter a number and have the program generate PI up to that many decimal places.
Keep a limit to how far the program will go.
- I used the Machin formula found here:
http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/fibpi.html#machin

Call By
- python
- from numbers.find_pi import find_pi
- find_pi(length)

"""
from math import atan


def find_pi(length):
    _pi = 4 * (4 * (atan(1.0 / 5.0)) - atan(1.0 / 239.0))
    print ('{0:.%df}' % length).format(_pi)
