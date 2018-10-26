import json
from pprint import pprint

with open('jsons\db.json') as f:
    data = json.load(f)

for i in range(1,10):
    print(data['%d'%(i)]['id'])
    print(data['%d'%(i)]['author'])
    print(data['%d'%(i)]['created_utc'])
    print(data['%d'%(i)]['ups'])
    print(' ')
