import json
import csv
from config import congress


senate = congress.members.filter('senate')

header = ['Name', 'Party', 'State', 'District', 'Title']

with open('csv/senate.csv', mode='w') as senate_file:
    senate_writer = csv.DictWriter(senate_file, fieldnames=header)

    senate_writer.writeheader()

    for member in senate[0]['members']:
        memberDict = {'Name': member['first_name'] + " " + member['last_name'],
                      'Party': member['party'],
                      'State': member['state'],
                      'Title': member['title'].replace(', ',' - ')}
        senate_writer.writerow(memberDict)
