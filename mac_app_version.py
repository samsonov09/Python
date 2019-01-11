#!/usr/bin/python3.7

import os, sys
from plistlib import load

'''
All rights reserved © 2018 
'''

path = '/Applications/'
files = os.listdir(path)
x = 0
z = 0
app = [None] * len(files)
app0 = [None] * len(files)

print("\nApplication List: \n")

for name in files:
    plist = (path + name +  '/Contents/Info.plist')
    app[x] = plist
    x = x + 1
for i in range(len(app)):
    if os.path.exists(app[i]):
        with open(app[i], 'rb') as fp:
            pl = load(fp)
            x = pl["CFBundleShortVersionString"]
            # resolve it  if does not exist than say, app name not found
            y = pl["CFBundleExecutable"]

            print ("\t" + str(i + 1 ) + ") "  + y + " - version:  " + x)
    else:
        app0[z] = " \t Warning - " + app[i] + " value does not exist "
        z = z + 1


for t in range(len(app0)):
    if sys.getsizeof(app0[t]) > 16:
        print(app0[t])
