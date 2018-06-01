import os
from os.path import isfile, join
import datetime

folder = input('Folder path: ')
path = 'C:/Users/David/Documents/Python/' + folder
os.chdir(path)
print(os.getcwd())

files = [f for f in os.listdir() if isfile(join(f))]
bikeID = input('BikeID: ')
device = input('Device: ')
serial = input('Last 4 serial #: ')
date = ''
while True:
    samedate = input('Using today\'s date? (Y/N)')
    if samedate.lower() == 'y':
        date = datetime.datetime.today().strftime('%y%m%d')
    elif samedate.lower() == 'n':
        date = input('Date: ')
    break
ext = input('Extension: ')
for f in range(len(files)):
    print('\n'+files[f])
    session = input('Session: ')
    filename = '{}_{}_{}_S{}_{}.{}'.format(bikeID, device, serial, session, date, ext)
    os.rename(files[f], filename)
