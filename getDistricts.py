import json
import csv
from config import congress


house = congress.members.filter('house')

header = ['Name', 'State', 'Zip']

with open('csv/districts.csv', mode='w') as district_file:
    district_writer = csv.DictWriter(district_file, fieldnames=header)

    district_writer.writeheader()

    for member in house[0]['members']:
        if member['district'] == 'At-Large':
            member['district'] = 'AL'
        elif int(member['district']) < 10:
            member['district'] = "0" + member['district']
        memberDict = {
                      'State': member['state'],
                      'Name': member['state'] + "_" + member['district'],
                      }
        district_writer.writerow(memberDict)
