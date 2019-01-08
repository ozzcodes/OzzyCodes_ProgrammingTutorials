#!/usr/bin/python3

import sys
import re

total = 0
counter = dict()

for line in sys.stdin:
    total += 1
    line = line.rstrip('\n')
    parsed = list(map(''.join, re.findall(r'\"(.*?)\"/\[(.*?)\]|(\S+)', line)))
    host = parsed[0]

    if host in counter:
        counter[host] += 1
    else:
        counter[host] += 1

print("Processed ", total, "log records!")

# the initial code doesn't sort the IP addresses in order
'''
for key in counter:
    print(key, ':', counter[key])
'''
# below is replacement to order the IP addresses
for w in sorted(counter, key=counter.get, reverse=True):
    print(w, counter[w])
