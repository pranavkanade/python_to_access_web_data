import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'

url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
url2 = 'http://py4e-data.dr-chuck.net/comments_111183.xml'

# addr = serviceurl + urllib.parse.urlencode({'address': url})
xml_data = urllib.request.urlopen(url2).read().decode()
# print(xml_data)
tree = ET.fromstring(xml_data)

results = tree.findall('comments/comment')
# print(len(results))
list_counts = [int(r.find('count').text) for r in results]
print(sum(list_counts))
# while True:
#     address = input('Enter location: ')
#     if len(address) < 1: break

#     url = serviceurl + urllib.parse.urlencode({'address': address})
#     print('Retrieving', url)
#     uh = urllib.request.urlopen(url)
#     data = uh.read()
#     print('Retrieved', len(data), 'characters')
#     print(data.decode())
#     tree = ET.fromstring(data)

#     results = tree.findall('result')
#     lat = results[0].find('geometry').find('location').find('lat').text
#     lng = results[0].find('geometry').find('location').find('lng').text
#     location = results[0].find('formatted_address').text

#     print('lat', lat, 'lng', lng)
#     print(location)