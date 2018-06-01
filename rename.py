import os
from os.path import isfile, join
import datetime

files = [f for f in os.listdir() if isfile(join(f))]
newname = []
bikeID = newname.append(input('BikeID: '))
device = newname.append(input('Device: '))
serial = newname.append(input('Last 4 serial #: '))
while True:
    samedate = input('Using today\'s date? (Y/N)')
    if samedate.lower() == 'y':
        date = newname.append(datetime.datetime.today().strftime('%y%m%d'))
        break
    elif samedate.lower() == 'n':
        date = newname.append(input('Date: '))
        break
ext = input('extension: ')
for file in range(len(files)):
    print('\n'+files[file])
    session = input('Session: ')
    newname.insert(3, 'S' + session)
    filename = '_'.join(newname) + '.' + ext
    os.rename(files[file], filename)
    del newname[3]
