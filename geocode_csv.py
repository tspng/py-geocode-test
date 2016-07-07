#!/usr/bin/env python
import sys
import geocoder
import unicodecsv as csv


def geocode_csv(filename):
    with open(filename) as f:
        reader = csv.reader(f, encoding='utf-8')
        # Skip header row if needed
        reader.next()
        for row in reader:
            # Build name and address to get coordinates from
            geoname = ','.join(row)
            print(u"trying to get lat/lng of {}".format(geoname))
            g = geocoder.google(geoname)
            # See documentation: http://geocoder.readthedocs.io/api.html#forward-geocoding
            print(g.latlng)


if __name__ == '__main__':
    try:
        in_csv = sys.argv[1]
    except IndexError:
        print("Usage: {} CSV_FILE".format(sys.argv[0]))
    geocode_csv(in_csv)
