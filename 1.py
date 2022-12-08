from time import sleep
import json

with open("users.txt", "r") as f:
    d = json.loads(f.read())
    cnt = 0
    for k in d.keys():
        if len(d[k]) > 0:
            cnt += 1
    print(cnt)