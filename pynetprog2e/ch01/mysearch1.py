import googlemaps

# Variables
myaddress = '2084 Huntingdon Dr., Wixom, MI 48393'

gmclient = googlemaps.Client(key='AIzaSyDhMDnzWJqQAPNCn_jq_mTRBYPiMgIHKRI')
mygeocoords = googlemaps.geocoding.geocode(gmclient,address=myaddress)

print 'Geocoordinates for address ' + myaddress + ':'
print mygeocoords[0]['geometry']['location']

