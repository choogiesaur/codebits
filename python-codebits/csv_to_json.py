import json
import csv

# Read CSV file
with open('test.csv', 'r') as f:
    reader = csv.reader(f)

    # Stores first row, increments reader to next row
    headers = next(reader)
    print(headers)

    # Dictionary to hold csv data, will be dumped to JSON
    data = {"names":[]}

    # Reads starting from 2nd row
    for row in reader:
        data["names"].append(
            {"firstname": row[0], "age":row[1]}
        )
    
    print(data)

# Dump data dictionary to file object f with indent level 4
with open('out.json', 'w') as f:
    json.dump(data, f, indent=4)