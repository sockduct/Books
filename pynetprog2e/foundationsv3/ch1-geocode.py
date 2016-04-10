##############################################################################
#
# James Small
#
# Example Program
#
# Foundations of Python Network Programming, 3e
#
##############################################################################

#
# What's the lattitude and longitude for this postal address?
#
# Use Google's Geocoding API!
# http://code.google.com/apis/maps/documentation/geocoding/
#
# When looking to use new services/APIs - always start with with Python
# Standard Library:
# http://docs.python.org/2/library/
# http://docs.python.org/3/library/
#
# Next check the Python Package Index:
# https://pypi.python.org/
#
# Package for Google's Geocoding API
# http://pypi.python.org/pypi/pygeocoder/
#
# Test packages before installing them in your main python repository
# Use virtualenv package

# Used by printpostaladdr
from pygeocoder import Geocoder
#
# Used by mygeocode
import requests
#
# Used by mygeocode2
# Python 3 only
#import http.client
# Instead use older httplib for Python 2
import httplib
import json
# Python 3 only
#from urllib.parse import quote_plus
# Python 2
from urllib import quote_plus

##############################################################################
# Easy Button - Use pygeocoder package:
def printpostaladdr(postaladdr):
    print("Postal Address:\n" + mypostaladdr + "\nLatitude, Longitude " \
        "coodinates:  " + \
        str(Geocoder.geocode(mypostaladdr)[0].coordinates))

##############################################################################
# Next layer down, make the request to Google myself:
def mygeocode(postaladdr):
    parameters = {'address': postaladdr, 'sensor': 'false'}
    base = 'http://maps.googleapis.com/maps/api/geocode/json'
    response = requests.get(base, params=parameters)
    answer = response.json()
    print(answer['results'][0]['geometry']['location'])

##############################################################################
# Next layer down, build the http request to Google myself:
# Note:  Doesn't work - see booksrc/search3.py
def mygeocode2(postaladdr):
    base = '/maps/api/geocode/json'
    path = '{}?postaladdr={}&sensor=false'.format(base, quote_plus(postaladdr))
    # Python 3
    #connection = http.client.HTTPConnection('maps.google.com')
    # Python 2
    connection = httplib.HTTPConnection('maps.google.com')
    connection.request('GET', path)
    rawreply = connection.getresponse().read()
    reply = json.loads(rawreply.decode('utf-8'))
    #print(reply['results'][0]['geometry']['location'])
    print(reply)

##############################################################################
# Use this to make this program module friendly
# Rather than having global code, use this to only execute global
# code if this program is executed directly.  If this program is
# imported as a module, the global code won't run.
# Global code can also be put in a main() procedure which can be
# called from this construct:
if __name__ == '__main__':
    mypostaladdr = '2084 Huntingdon Dr., Wixom, MI 48393'
    #print "Easy Way - Use Geocoder Package:"
    #printpostaladdr(mypostaladdr)
    #print "\nMore Work - Write our own procedure:"
    #mygeocode(mypostaladdr)
    print "\nMore Work - Write our own procedure and build http request:"
    mygeocode2(mypostaladdr)

