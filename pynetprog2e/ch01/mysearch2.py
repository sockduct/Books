import urllib, urllib2
import json

# Old (v2?)
#params = {'q': '207 N. Defiance St, Archbold, OH', 'output': 'json', 'oe': 'utf8'}
params = {'address': '207 N. Defiance St, Archbold, OH', 'key': 'AIzaSyDhMDnzWJqQAPNCn_jq_mTRBYPiMgIHKRI'}
# Old (v2?) - doesn't work
#url = 'http://maps.google.com/maps/geo?' + urllib.urlencode(params)
url = 'https://maps.googleapis.com/maps/api/geocode/json?' + urllib.urlencode(params)

rawreply = urllib2.urlopen(url).read()
reply = json.loads(rawreply)
# Old (v2?)
#print reply['Placemark'][0]['Point']['coordinates'][:-1]
print reply['results'][0]['geometry']['location']

