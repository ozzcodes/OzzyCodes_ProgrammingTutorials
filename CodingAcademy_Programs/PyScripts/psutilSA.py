#!/usr/bin/python3

import psutil

for x in range(5):
    print(psutil.cpu_percent(interval=1))

for x in range(2):
    print(psutil.virtual_memory())

print(psutil.net_connections())
p = psutil.Process(1)
print(p.name(), p.uids())
