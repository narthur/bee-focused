#!/usr/bin/env python3

import json
from pprint import pprint
import urllib.request
import os

json_data = open("auth_token.json").read()
data = json.loads(json_data)
auth_token = data['auth_token']
username = data['username']

goals_json = open("goals.json").read()
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

print('Lowest lane: %s' % lowestLane)

if lowestLane < 0:
    print('Time to focus!')
    os.system("open focus://focus")
else:
    print('Good job! Unfocusing...')
    os.system("open focus://unfocus")