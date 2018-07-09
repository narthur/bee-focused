#!/usr/bin/env python3

import json
from pprint import pprint
import urllib.request
import os
import datetime

print('----------')
print(datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y"))

dir = os.path.dirname(os.path.abspath(__file__))

json_data = open('%s/auth_token.json' % dir).read()
data = json.loads(json_data)
auth_token = data['auth_token']
username = data['username']

goals_json = open('%s/goals.json' % dir).read()
goals = json.loads(goals_json)
pprint(goals)

lowestLane = 0
for goal in goals:
    url = 'https://www.beeminder.com/api/v1/users/%s/goals/%s.json?auth_token=%s' % (username, goal, auth_token)
    result = urllib.request.urlopen(url).read()
    result_data = json.loads(result);
    lane = result_data['lane']
    print('%s: %d' % (goal, lane))
    lowestLane = lowestLane if lowestLane < lane else lane

if lowestLane < 0:
    print('Time to focus!')
    os.system("open focus://focus?minutes=7")
else:
    print('Good job! Focus session should expire in ~2 minutes.')
