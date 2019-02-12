from bs4 import BeautifulSoup
import urllib.request
import time

html = urllib.request.urlopen('http://www.nbclosangeles.com/news/top-stories/?rss=1')

soup = BeautifulSoup(html, 'xml')

for item in soup.findAll('link')[3:]:
    url = item.text
    news = urllib.request.urlopen(url).read()

    print(news)
    print(20 * '#')

    page = BeautifulSoup(news)

    for p in page.findAll('p'):
        print(p.text)

    time.sleep(10)
