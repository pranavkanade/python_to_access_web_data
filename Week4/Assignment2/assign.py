import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
from pprint import pprint
import re

def extraction_func(url_test, pos):
    html = urllib.request.urlopen(url_test).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    href_list = list()
    # pprint(tags[:5])
    for tag in tags:
        href_list.append(str(tag.get('href', None)))
    return href_list[pos-1] , re.findall('>(.*)<', str(tags[pos-1]))[0]

url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
url2 = 'http://py4e-data.dr-chuck.net/known_by_Aelish.html'

result_list = list()
position = 18
count = 7

for i in range(count):
    url2, res = extraction_func(url2, position)
    result_list.append(res)

# print(result_list)
print(result_list[-1])