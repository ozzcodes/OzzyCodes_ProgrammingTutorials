#!/usr/bin/python3

import os
import sys
import pwd

if len(sys.argv) >= 2:
    directory = str(sys.argv[1])
else:
    print('Not enough arguments!')
    sys.exit(0)

noByte = 0
fileName = ''
owner = 'www-data'

for root, dirs, files in os.walk(directory):
    for file in files:
        pathname = os.path.join(root, file)
        if os.path.exists(pathname):
            st = os.stat(pathname)
            try:
                userinfo = pwd.getpwuid(st.st_uid)
                ownername = pwd.getpwuid(st.st_uid).pw_name
            except:
                print('Unexpected Error!', sys.exc_info()[0], pathname)
                if(ownername != owner) and (ownername != 'root'):
                    print(pathname)
                    print('Owner: ', ownername)

