from time import sleep
import json

from lib.Parser import Parser

parser = Parser()

with open("groups.txt") as f:
    groups = list(set([x.strip().split('/')[-1] for x in f.readlines()]))

gids = []
for group in groups:
    gids.append(parser.getGroupId(group))
    sleep(1)

a = dict()
for gid in gids:
    a[gid] = parser.getGroupMembers(gid)

with open("users.txt", "w") as f:
    f.write(json.dumps(a))