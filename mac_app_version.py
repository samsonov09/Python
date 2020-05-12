#!/usr/bin/python3.7

import os
import sys
from plistlib import load

'''
All rights reserved © 2018 
'''

path = '/Applications/'
files = os.listdir(path)

x = 0

app = [None] * len(files)
app0 = [None] * len(files)

print("\nApplication List:")

for name in files:
    plist = (path + name + '/Contents/Info.plist')
    app[x] = plist
    x = x + 1

for i in range(len(app)):
    if os.path.exists(app[i]):
        with open(app[i], 'rb') as fp:
            pl = load(fp)
            app_name = pl["CFBundleExecutable"]
            app_name = str(app_name)
            app_version = pl["CFBundleShortVersionString"]
            print(app_version, '\n')
            if app_version != 0:
                i = str(i + 1)
            print("\t" + i + ") " + app_name + " - version:  " + app_version)
    else:
        app0 = " \t Warning - ", app_name, " value does not exist "

for t in range(len(app0)):
    if sys.getsizeof(app0[t]) > 16:
        print(app0[t])
