import json
import datetime
import time

import sys

try:
    day = sys.argv[1]
except:
    day = "1"

today = datetime.date(2022,12,int(day))


def get_t(day, part):
    try:
        # return datetime.date.fromtimestamp(int(day[str(part)]['get_star_ts'])).strftime("%H:%I:%S")
        return int(day[str(part)]['get_star_ts'])
    except:
        return None

def get_ts(day, part):
    try:
        # return datetime.date.fromtimestamp(int(day[str(part)]['get_star_ts'])).strftime("%H:%I:%S")
        ts = get_t(day, part)
        lt = time.localtime(ts)
        # datetime
        # print(lt - today)

        return time.asctime(time.localtime(ts))
    except:
        return ""



names=["Håkan Lundvall",]

res = []
lb = json.loads(open("lb.json", "r").read())
members = lb['members']
for k in members:
    member = members[k]
    try:
        if member['name'] in names or "1" in member['completion_day_level'][day].keys():
            sc = [(x, get_ts(y,1), get_ts(y,2), get_t(y, 1), get_t(y, 2)) for x, y in member['completion_day_level'].items() if x == str(day)]  
            if   member['name']:
                res.append((member['name'], *sc[0][1:]))
            else:
                res.append((member['id'], *sc[0][1:]))

    except:
        pass

print("Part 1")
for n, x in enumerate(sorted(res, key = lambda i: i[3])):
    y = [a if a else "None" for a in x]
    print("{:<3} {:<20} {}, {}".format(n+1, *y))

print("\nPart 2")

for n, x in enumerate(sorted(filter(lambda x: x[4], res), key = lambda i: i[4])):
    y = [a if a else "None" for a in x]
    print("{:<3} {:<20} {}, {}".format(n+1, *y))
