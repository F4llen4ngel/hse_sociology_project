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

print(len(groups))
names = pr.getGroupNames(groups)

with open("group_names.txt", "w") as f:
    f.write(json.dumps(names))