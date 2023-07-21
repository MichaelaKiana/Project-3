# Libraries to import
import json

# Merge two json files, richard-bachman.json and stephen-king.json
# and write the merged data to a new file, king-bachman.json

# Open the first file
with open('richard-bachman.json') as json_file:
    data1 = json.load(json_file)

# Open the second file  
with open('stephen-king.json') as json_file:
    data2 = json.load(json_file)

# Merge the two files into a new file
merged_data = []
merged_data.extend(data1)
merged_data.extend(data2)

# Write the merged data to a new file
with open('king-bachman.json', 'w') as outfile:
    json.dump(merged_data, outfile)




