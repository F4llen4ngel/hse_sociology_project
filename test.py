from time import sleep
import json
import os

from lib.Parser import Parser

parser = Parser()

with open("groups.txt") as f:
    groups = list(set([x.strip().split('/')[-1] for x in f.readlines()]))

gids = []
for group in groups:
    gids.append(parser.getGroupId(group))

with open("group_users.txt", "r") as f:
    d = json.loads(f.read())

users = []
for gid in gids:
    try:
        users += d[str(gid)]
    except:
        pass  

print(len(users))

subs = dict()

for i in range(len(users)):
    subs[users[i]] = parser.getUserGroups(users[i])
    os.system('cls')
    print(f"[progress]: {round(i * 100 / len(users), 3)}%...")

with open("users.txt", "w") as f:
    f.write(json.dumps(subs)) 