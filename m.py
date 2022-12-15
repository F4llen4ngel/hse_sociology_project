import json

result = {}

count_left = 0
count_right = 0
not_found = 0

GOOD_GROUPS = ["za", "russia", "zo", "путин", "русский", "горжусь", "родина", "нац", "патриот"]

def classificate(groups):
    return any([any([sub in group.lower() for sub in GOOD_GROUPS]) for group in groups])

group_names = json.load(open("group_names.txt", "r"))
print(1)
group_users = json.load(open("group_users.txt", "r"))
print(2)
with open("users.txt", "r") as f:
    users = json.loads(f.read())

for group, users_list in group_users.items():
    new_group_l = 0
    new_group_n = 0
    print("looking for liberals in the group", group)
    for user in users_list:
        user_groups_ids = users[str(user)]
        user_groups_names = []
        for user_group_id in user_groups_ids:
            try:
                user_groups_names.append(group_names[str(user_group_id)][0])
            except:
                pass
        if len(user_groups_names) < 3:
            not_found += 1
            continue
        if classificate(user_groups_names):
            new_group_n += 1
        else:
            new_group_l += 1
    result[group] = [new_group_l, new_group_n]
    count_left += new_group_l
    count_right += new_group_n

print(result, count_left, count_right, not_found)
