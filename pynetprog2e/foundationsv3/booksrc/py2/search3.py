#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter01/search3.py

from __future__ import absolute_import
import httplib
import json
from urllib import quote_plus

base = u'/maps/api/geocode/json'

def geocode(address):
    path = u'{}?address={}&sensor=false'.format(base, quote_plus(address))
    connection = httplib.HTTPConnection(u'maps.google.com')
    connection.request(u'GET', path)
    rawreply = connection.getresponse().read()
    reply = json.loads(rawreply.decode(u'utf-8'))
    print reply[u'results'][0][u'geometry'][u'location']

if __name__ == u'__main__':
    geocode(u'207 N. Defiance St, Archbold, OH')
