# Python script to prepare JSON content

from os import listdir, remove
from os.path import isfile, join
import json

mypath = '/Users/Jeroennieboer/Documents/openbanking/branches/barclays'

files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

data_prev = {}
duplicates = []

for f in files:
  with open(mypath + '/' + f) as json_file:
    contents = json.load(json_file)
    if ("data" in contents):
      data = contents['data']
    else:
      data = contents['src/main/resources/data'] # To deal with historical Barclays bug

    if ((data_prev != {}) & (data == data_prev)) : 
      duplicates.append(mypath + '/' + f)
    data_prev = data

for d in duplicates:
  remove(d)
  
  
