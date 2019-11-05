import json
import csv
from config import congress


house = congress.members.filter('house')

header = ['Name', 'Party', 'State', 'District', 'Title', 'Website', 'Facebook', 'Twitter']

with open('csv/house-socials.csv', mode='w') as house_file:
    house_writer = csv.DictWriter(house_file, fieldnames=header)

    house_writer.writeheader()

    for member in house[0]['members']:
        memberDict = {
                      'Name': member['first_name'] + " " + member['last_name'],
                      'Website': member['url'], 'Facebook': member['facebook_account'], 'Twitter': member['twitter_account']}
        house_writer.writerow(memberDict)
