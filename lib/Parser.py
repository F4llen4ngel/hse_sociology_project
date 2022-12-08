from fake_useragent import UserAgent
import requests
import json
from time import sleep

class Parser:

    def __init__(self): 
        with open("access.token") as f:
            self.access_token = f.read()
        self.user_agent = UserAgent().chrome
        self.headers = {'User-Agent': self.user_agent}
    
    def request(self, url):
        raw = requests.get(url, headers=self.headers)
        try:
            resp = json.loads(raw.text)["response"]
        except:
            resp = None
            print(raw.text)
        sleep(0.33)
        return resp

    def getUserGroups(self, user_id):
        url = f"https://api.vk.com/method/users.getSubscriptions?&access_token={self.access_token}&user_id={user_id}&v=5.131"
        resp = self.request(url)
        if resp is None:
            return []
        return resp["groups"]["items"]

    def getGroupMembers(self, group_id):
        offset = 0
        url = f"https://api.vk.com/method/groups.getMembers?&access_token={self.access_token}&group_id={group_id}&offset={offset}&v=5.131" 
        resp = self.request(url)
        if resp is None:
            return []
        membersList = resp["items"]
        count = resp["count"]
        for offset in range(1000, count, 1000):
            url = f"https://api.vk.com/method/groups.getMembers?&access_token={self.access_token}&group_id={group_id}&offset={offset}&v=5.131"
            resp = self.request(url)
            membersList += resp["items"]
        return membersList

    def getGroupId(self, group_name):
        url = f"https://api.vk.com/method/utils.resolveScreenName?&access_token={self.access_token}&screen_name={group_name}&v=5.131"
        resp = self.request(url)
        return resp["object_id"]

    def getGroupName(self, group_id):
        url = f"https://api.vk.com/method/groups.getById?&access_token={self.access_token}&group_id={group_id}&v=5.131"
        resp = self.request(url)
        return (resp["name"], resp["screen_name"])

    def chunks(self, arr):
        for i in range(0, len(arr), 25):
            yield arr[i:i+25]

    def getGroupNames(self, groups):
        names = dict()
        for chunk in self.chunks(groups):
            names |= self.executeGroupNames(chunk)
        return names

    def executeGroupNames(self, groups):
        assert len(groups) <= 25, "can't execute more than 25 requests per procedure"
        url = f"https://api.vk.com/method/execute.groupNames?access_token={self.access_token}&groups={','.join(list(map(str, groups)))}&v=5.131"
        resp = self.request(url)
        names = dict()
        for g in resp:  
            names[g["id"]] = (g["name"], g["screen_name"])
        return names