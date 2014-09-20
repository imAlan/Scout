import urllib
import json


def get_latlng(address):
    URL2 = "https://maps.googleapis.com/maps/api/geocode/json?address=" + address + "&sensor=false"
    googleResponse = urllib.urlopen(URL2)
    jsonResponse = json.loads(googleResponse.read())
    test = json.dumps([s['geometry']['location'] for s in jsonResponse['results']], indent=3)
    if test:
        x = test
        x = x.split()
        try:
            lat = x[3].strip(',')
        except IndexError:
            lat = ''
        try:
            lng = x[5]
        except IndexError:
            lng = ''
        return lat, lng