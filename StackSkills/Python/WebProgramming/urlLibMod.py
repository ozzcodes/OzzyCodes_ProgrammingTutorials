import urllib.request
import urllib

req = urllib.request.urlopen('https://www.google.com')
print(req.read())
