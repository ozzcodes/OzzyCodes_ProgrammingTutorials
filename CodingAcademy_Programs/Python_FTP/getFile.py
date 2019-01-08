#!/usr/bin/python3

import sys
from ftplib import FTP

site = str(sys.argv[1])
connection = FTP(site)
connection.login("anonymous", "aMail@gmail.com")
print("Connected to %s" % site)

# Change current directory
newDirectory = '/pub/www'
connection.cwd(newDirectory)

file = '00_index.txt'
localfile = open(file, 'wb')
print("Downloading... %s from %s" % (file, newDirectory))

connection.retrbinary('RETR' + file, localfile.write, 1024)
connection.close()
localfile.close()
