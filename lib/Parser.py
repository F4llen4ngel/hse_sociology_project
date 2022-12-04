from fake_useragent import UserAgent
import requests
import json

class Parser:

    def __init__(self): 
        with open("access.token") as f:
            self.access_token = f.read()
        self.user_agent = UserAgent().chrome
        self.headers = {'User-Agent': self.user_agent}
    
    def getUserGroups(self, user_id):
        url = f"https://api.vk.com/method/users.getSubscriptions?&access_token={self.access_token}&user_id={user_id}&v=5.131"
        raw = requests.get(url, headers=self.headers)
        groupsList = json.loads(raw.text)
        return groupsList["response"]["groups"]["items"]

    def getGroupMembers(self, group_id):
        offset = 0
        url = f"https://api.vk.com/method/groups.getMembers?&access_token={self.access_token}&group_id={group_id}&offset={offset}&v=5.131"
        raw = requests.get(url, headers=self.headers) 
        resp = json.loads(raw.text)["response"]
        membersList = resp["items"]
        count = resp["count"]
        for offset in range(1000, count, 1000):
            url = f"https://api.vk.com/method/groups.getMembers?&access_token={self.access_token}&group_id={group_id}&offset={offset}&v=5.131"
            raw = requests.get(url, headers=self.headers) 
            resp = json.loads(raw.text)["response"]
            membersList += resp["items"]
        return membersList
