import requests
import pytz
from datetime import datetime
import json


class Contest:
    def __init__(self, id, name, platform, link, startTime, endTime):
        self.id = id
        self.name = name
        self.platform = platform
        self.link = link
        self.startTime = startTime
        self.endTime = endTime



TIME_FORMAT = '%Y-%m-%dT%H:%M:%S'
epoch = datetime.utcfromtimestamp(0)

def getTimeInMillis(time_str):
    time_object = datetime.strptime(time_str, TIME_FORMAT)
    return int((time_object-epoch).total_seconds()*1000)

'''
Meta: 133
codeforces: 1
codechef: 2
leetcode: 102
google: 35
atcoder: 93
'''
clistId_to_platform_id = {
    1: 1,
    2: 2,
    93: 3,
    102: 4,
    35: 5,
    133: 6
}
clistId_to_platform_name = {
    1: 'Codeforces',
    2: 'Codechef',
    93: 'Atcoder',
    102: 'Leetcode',
    35: 'Google',
    133: 'Meta'
}

def getPlatformIdFromResourceId(clistId):
    return clistId_to_platform_id.get(clistId, -1)

def getPlatformNameFromResourceId(clistId):
    return clistId_to_platform_name.get(clistId, 'Platform not supported')

    
URL = "https://clist.by:443/api/v2/contest/?limit=300&start_time__during=8640000&resource_id__in=1%2C2%2C93%2C102%2C133%2C35&filtered=false&order_by=-start&username=MaskedCarrot&api_key=3756ead7ff87d60d0029be2c4d3b6847ad6aa1b5"

data = requests.get(url = URL).json()
processedData = {'contests': []}

for d in data['objects']:    
    if (getPlatformIdFromResourceId(d['resource_id']) == -1): 
            continue
    processedData['contests'].append(
        Contest(
            id=getPlatformIdFromResourceId(d['resource_id']),
            name=d['event'],
            platform=getPlatformNameFromResourceId(d['resource_id']),
            link=d['href'],
            startTime=getTimeInMillis(d['start']),
            endTime=getTimeInMillis(d['end'])
        ).__dict__
    )
    
with open('data/contests.json', 'w') as outfile:
    json.dump(processedData, outfile, indent=4)
