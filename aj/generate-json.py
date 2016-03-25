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

        display_name = u'{} ({})'.format(row['HomeKit Name'], row['Geschoss'])

        if row['HomeKit Type'] == 'Lightbulb':
            d = {
                "description": display_name,
                "name": display_name,
                "services": [
                        {
                                "type": row['HomeKit Type'],
                                "description": display_name,
                                "name": row['HomeKit Name'],
                                "On": {
                                        "Set": row['GA Schalten'],
                                        "Listen": [
                                                row['GA RM']
                                         ]
                                 }
                         }
                ],
                "services-description": display_name
            }
        elif row['HomeKit Type'] == 'Temperature Sensor':
            d = {
                "description": display_name, 
                "name": display_name,
                "services": [
                        {
                                "type": "TemperatureSensor",
                                "description": display_name,
                                "name": row['HomeKit Name'],
                                "CurrentTemperature": {
                                        "Set": "",
                                        "Listen": [
                                                row['GA Schalten']
                                         ]
                                 }
                         }
                ],
                "services-description": display_name
            }
        else:
            continue

        print d
        accessories.append(d)

result = template.copy()
result['platforms'][0]['accessories'] = accessories

with open('config-out.json', 'wb') as fp:
    json_data = json.dumps(result, indent=4, ensure_ascii=False)
    fp.write(json_data.encode('utf8'))
