#!/usr/bin/python                                                               

# Load the JSON module and use it to load your JSON file.                       
# I'm assuming that the JSON file contains a list of objects.                   
import json
obj  = json.load(open("data.json"))

# Iterate through the objects in the JSON and deletes keys
# the obj once we find it.

for i in range(len(obj)):
    test = obj[i]
    if any(obj[i][j] == 'bundle-name' for j in obj[i]):
        del obj[i]['bundle-name']
    if any(obj[i][j] == 'isKeyRevealed' for j in obj[i]):
        del obj[i]['isKeyRevealed']

#sorts the array to a list
sorted_array = sorted(obj, key=lambda x: x['name'])
obj = sorted_array

# Output the updated file with pretty JSON                                      
open("updated-file.json", "w").write(
    json.dumps(obj, sort_keys=True, indent=4, separators=(',', ': '))
)
