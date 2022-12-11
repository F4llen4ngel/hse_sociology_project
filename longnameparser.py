from lib.Parser import Parser
import json
import os

pr = Parser()

with open("users.txt", "r") as f:
    d = json.loads(f.read())

groups = []
for i in d.values():
    groups += i
groups = list(set(groups))

names = dict()

for i in range(len(groups)):
    os.system("cls")
    gid = groups[i]
    names[gid] = pr.getGroupName(gid)
    print(f"[progress]: {round(i * 100 / len(groups), 3)}%...")