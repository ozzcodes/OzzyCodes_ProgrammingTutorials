file = open("lxf-test.txt", "w")

feeds = ["http://newsrss.bbc.co,uk/rss/newsonline_uk_edition/front_page/"
         "rss.xml", "http://www.tuxradar.com/rss"]

for feed in feeds:
    file.write("{0}\n".format(feed))

file.close()

'''
lookup Python list comprehensions - use of opening
and closing a file withing a 'with' loop
'''
