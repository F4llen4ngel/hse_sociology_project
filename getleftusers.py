from lib.Parser import Parser
from random import randint


with open("leftusers.txt", "r") as f:
     usr = f.read().split(", ")


l = [usr[randint(0, len(usr) - 1)] for _ in range(150)]
pr = Parser()
gr = {}


for user in l:
    groups = pr.getUserGroups(user)
    for g in groups:
        if g not in gr.keys():
            gr[g] = 1
        else:
            gr[g] += 1

ans = [g for g in gr.keys() if gr[g] > 15]
print(ans)