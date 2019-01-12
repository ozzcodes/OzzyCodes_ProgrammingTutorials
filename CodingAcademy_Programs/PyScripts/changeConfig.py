#!/usr/bin/python3

import configparser
from itertools import chain

parser = configparser.ConfigParser()
with open("./mongodb.conf") as lines:
    parser.read_file(lines)

print("dbpath: ", parser.get('MongoDB', 'dbpath'))
parser.set('MongoDB', 'dbpath', '/tmp')
print("New dbpath: ", parser.get('MongoDB', 'smallfiles'))
print("smallfiles: ", parser.get('MongoDB', 'smallfiles'))
parser.remove_option('MongoDB', 'smallfiles')

with open('./mongodb.conf', 'w') as configfile:
    parser.write(configfile)
