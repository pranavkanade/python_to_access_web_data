from urllib.request import urlopen
from bs4 import BeautifulSoup
# import ssl 
from pprint import pprint
import re
# Following code block to ignore the SSL certificate errors
# ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
# ctx = False
# ctx.verify_mode = ssl.CERT_NONE

# orig code

url = 'http://py4e-data.dr-chuck.net/comments_42.html'
url2 = 'http://py4e-data.dr-chuck.net/comments_111181.html'

data_html = urlopen(url2).read()
# pprint(data_html.decode())
# count = sum(list(map(int, re.findall('\d+', data_html.decode()))))

# print(count)
soup = BeautifulSoup(data_html, 'html.parser')
# pprint(str(list(soup('span'))[0]))
count = 0
for element in list(map(str, list(soup('span')))):
    count += int(re.findall('\d+', element)[0])
print(count)