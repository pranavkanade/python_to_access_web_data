import urllib.request, urllib.parse, urllib.error
import json
from pprint import pprint
# Note that Google is increasingly requiring keys
# for this API
serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'

address = 'South Federal University'
address2 = 'EM Lyon'
url = serviceurl + urllib.parse.urlencode(
    {'address': address2})

json_data = json.loads(urllib.request.urlopen(url).read().decode())
pprint(json_data['results'][0]['place_id'])