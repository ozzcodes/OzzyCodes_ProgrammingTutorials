import urllib.request
import urllib.parse

url = 'https://www.google.com/search'
values = {'q': 'Python programming tutorials'}

# Internet uses UTF-8 format
data = urllib.parse.urlencode(values)
# Data sent to internet needs to be sent in UTF-8
# data = data.encode('utf-8')

# Headers are defined as dictionary
headers = {'User-Agent': "Mozilla/5.0 (X11; linux i686"}

req = urllib.request.Request(url, headers=headers)
resp = urllib.request.urlopen(req)
resp_data = resp.read()

print(resp_data)
