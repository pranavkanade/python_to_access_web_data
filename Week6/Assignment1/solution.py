import urllib.request, urllib.parse
import json

url = 'http://py4e-data.dr-chuck.net/comments_42.json'
url2 = 'http://py4e-data.dr-chuck.net/comments_111184.json'

json_data = json.loads(urllib.request.urlopen(url2).read().decode())

list_counts = list()

for comment in json_data['comments']:
    list_counts.append(int(comment['count']))

print(sum(list_counts))