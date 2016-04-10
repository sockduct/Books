import httplib
import json

# Old (v2?)
#path = ('/maps/geo?q=207+N.+Defiance+St%2C+Archbold%2C+OH&output=json&oe=utf8')
path = ('/maps/api/geocode/json?address=207+N.+Defiance+St%2C+Archbold%2C+OH'
        '&key=AIzaSyDhMDnzWJqQAPNCn_jq_mTRBYPiMgIHKRI')

# Old (v2?)
#connection = httplib.HTTPConnection('maps.google.com')
#connection = httplib.HTTPConnection('maps.googleapis.com')
# Must be over https, otherwise Google returns an error
connection = httplib.HTTPSConnection('maps.googleapis.com')
connection.request('GET', path)
rawreply = connection.getresponse().read()
reply = json.loads(rawreply)

# Old (v2?)
#print reply['Placemark'][0]['Point']['coordinates'][:-1]
print reply['results'][0]['geometry']['location']
#print reply

