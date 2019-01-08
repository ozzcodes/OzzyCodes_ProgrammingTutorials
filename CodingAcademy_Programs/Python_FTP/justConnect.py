#!/usr/bin/python3

import sys
from ftplib import FTP

site = str(sys.argv[1])
connection = FTP(site)
connection.login("anonymous", "aMail@gmail.com")
print("Connected to %s" % site)

files = []
files = connection.nlst()

for f in files:
    print(f)

connection.close()
