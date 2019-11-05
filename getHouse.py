import json
import csv
from config import congress


house = congress.members.filter('house')

header = ['Name', 'Party', 'State', 'District', 'Title', 'Website', 'Facebook', 'Twitter']
with open('csv/house.csv', mode='w') as house_file:
    house_writer = csv.DictWriter(house_file, fieldnames=header)

    house_writer.writeheader()

    for member in house[0]['members']:
        if member['district'] == 'At-Large':
            member['district'] = 'AL'
        elif int(member['district']) < 10:
            member['district'] = "0" + member['district']
        memberDict = {
                      'Name': member['first_name'] + " " + member['last_name'],
                      'Party': member['party'],
                      'State': member['state'],
                      'District': member['state'] + "_" + member['district'],
                      'Title': member['title'],'Website': member['url'], 'Facebook': member['facebook_account'], 'Twitter': member['twitter_account']}
        house_writer.writerow(memberDict)
