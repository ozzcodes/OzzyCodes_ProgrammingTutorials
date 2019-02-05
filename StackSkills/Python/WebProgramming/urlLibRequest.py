import urllib.request
import urllib.parse

url = 'https://www.google.com/search'
values = {'q': 'Python programming tutorials'}

# Internet uses UTF-8 format
data = urllib.parse.urlencode(values)
# Data sent to internet needs to be sent in UTF-8
data = data.encode('utf-8')

req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
resp_data = resp.read()

print(resp_data)
