# Prepare JSON content before Github upload

from os import listdir, remove
from os.path import isfile, join
import json

api_name = 'atms'
bank_name = 'barclays'
mypath = '/Users/Jeroennieboer/Documents/github/openbanking/data/raw/' + api_name + '/' + bank_name

files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

data_prev = {}
duplicates = []

for f in files:
  with open(mypath + '/' + f, 'r+') as json_file:
    contents = json.load(json_file)
    
    if ('src/main/resources/data' in contents):
      contents['data'] = contents.pop('src/main/resources/data') # To deal with historical Barclays bug

    # Flag duplicate files for deletion
    data = contents['data']
    if ((data_prev != {}) & (data == data_prev)) : 
      duplicates.append(mypath + '/' + f)
    data_prev = data
    
    # Re-save all files with nicer JSON formatting (indentation, newlines)
    json_file.seek(0) 
    json.dump(contents, json_file, ensure_ascii=False, indent=2)
    json_file.truncate()


for d in duplicates:
  remove(d)
