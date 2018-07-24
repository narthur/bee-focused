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

beeFocused = False
for goal in goals:
    goalName = goal["name"]
    targetBufferDays = goal["targetBufferDays"]
    url = 'https://www.beeminder.com/api/v1/users/%s/goals/%s.json?auth_token=%s' % (username, goalName, auth_token)
    result = urllib.request.urlopen(url).read()
    result_data = json.loads(result);
    lane = result_data['lane']
    loseTime = result_data['losedate']
    loseDate = datetime.datetime.fromtimestamp(loseTime)
    loseDateString = loseDate.strftime("%I:%M%p on %B %d, %Y")
    loseDateDelta = loseDate - datetime.datetime.now()
    bufferDays = loseDateDelta.days
    print("%s: You're going to lose in %d days (%s)" % (goalName, bufferDays, loseDateString))
    if bufferDays < targetBufferDays:
        print("%d days is less than %d days. Get focused!" % (bufferDays, targetBufferDays))
        beeFocused = True

if beeFocused:
    print('Time to focus!')
    os.system("open focus://focus?minutes=7")
else:
    print('Good job! Focus session should expire in ~2 minutes.')
