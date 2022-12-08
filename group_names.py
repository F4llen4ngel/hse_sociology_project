import json

from lib.Parser import Parser

parser = Parser()

with open("users.txt", "r") as f:
    d = json.loads(f.read())
    groups = set()
    for user in d.keys():
        for group in d[user]:
            groups.add(group)
    groups = list(groups)

names = parser.getGroupNames(groups)

with open("group_names.txt", "w") as f:
    f.write(json.dumps(names))