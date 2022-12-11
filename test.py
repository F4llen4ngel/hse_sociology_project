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

names = pr.getGroupNames(groups)