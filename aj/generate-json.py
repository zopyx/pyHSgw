import os
import sys
import csv
import json
import csv

with open('config.json', 'rb') as fp:
    template = json.load(fp)


accessories = list()

with open(sys.argv[-1], 'rb') as fp:
    reader = csv.DictReader(fp)

    for row in reader:

        row = row.copy()
        for k, v in row.items():
            row[k] = unicode(row[k], 'utf8')


        if row['Export'] != '1':
            continue

        d = {
            "description": row['Beschreibung'],
            "name": row['Beschreibung'],
            "services": [
                    {
                            "type": row['HomeKit Type'],
                            "description": row['Beschreibung'],
                            "name": row['HomeKit Name'],
                            "On": {
                                    "Set": row['GA Schalten'],
                                    "Listen": [
                                            row['GA RM']
                                     ]
                             }
                     }
            ],
            "services-description": row['Beschreibung']
        }
        print d
        accessories.append(d)

result = template.copy()
result['platforms'][0]['accessories'] = accessories

with open('config-out.json', 'wb') as fp:
    json_data = json.dumps(result, indent=4, ensure_ascii=False)
    fp.write(json_data.encode('utf8'))
