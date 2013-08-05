"""
Distance Between Two Cities
- Calculates the distance between two cities and allows the user to specify
a unit of distance. This program may require finding coordinates for the
cities like latitude and longitude.

This will require you to download the geopy module located here:
- https://code.google.com/p/geopy/
- pip install geopy

It uses the Haversine formula to find an approximate distance between the points.
- http://en.wikipedia.org/wiki/Haversine_formula

Call By
- python distance.py

"""
from geopy import geocoders
import math


def distance():
    point1 = raw_input('Enter a city and state ex: \'Tampa, FL\': ')
    point2 = raw_input('Enter another city and state ex: \'Tampa, FL\': ')

    # Convert the typed locations to coordinates
    try:
        g = geocoders.GoogleV3()
        place1, (lat1, lng1) = g.geocode(point1)
        place2, (lat2, lng2) = g.geocode(point2)

        # Radians measurements for angles
        lat1 = math.radians(lat1)
        lat2 = math.radians(lat2)
        lng1 = math.radians(lng1)
        lng2 = math.radians(lng2)

        # Haversine Formula
        a = (1 - math.cos((2 * (lat2 - lat1)) / 2.0)) / 2.0
        b = math.cos(lat1) * math.cos(lat2)
        c = (1 - math.cos((2 * (lng2 - lng1)) / 2.0)) / 2.0
        d = math.sqrt(abs(a + (b * c)))
        e = 2 * 6371 * math.asin(d)

        while True:
            output = raw_input('What units would you like the distance in? (Miles = M, Kilometers = KM): ').lower()

            if output not in ['m', 'km']:
                print 'Choose between K and M, please.'
            else:
                break

        if output == 'km':
            print '\nThe distance between {} and {} is:'.format(place1, place2)
            print '{0:.2f} km'.format(e)
        else:
            miles = e * 0.621371192
            print '\nThe distance between {} and {} is:'.format(place1, place2)
            print '{0:.2f} miles'.format(miles)

    except (ValueError, geocoders.base.GeocoderError):
        print 'We couldn\'t find one of those locations!'


if __name__ == '__main__':
    distance()
