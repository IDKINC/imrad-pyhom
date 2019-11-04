from config import congress

house = congress.members.filter('house')
senate = congress.members.filter('senate')
print(house[0])
print(senate[0])