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
            resp = json.loads(json.dumps(raw.text))[0]["response"]
        except Exception as e:
            resp = None
            print(e)
            print(type(json.loads(json.dumps(raw.text))))
            print(raw[:100])
        sleep(0.25)
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
        resp = self.request(url)[0]
        if resp is None:
            return ("", "")
        return (resp["name"], resp["screen_name"])


    def chunks(self, arr):
        for i in range(0, len(arr), 1000):
            yield arr[i:i+1000]
    
    def getGroupNamesChunk(self, group_ids):
        group_ids = ", ".join(list(map(str, group_ids)))
        url = f"https://api.vk.com/method/groups.getById?&access_token={self.access_token}&group_ids={group_ids}&v=5.131"
        resp = self.request(url)
        names = dict()
        for g in resp:
            names[g["id"]] = (g["name"], g["screen_name"])
        return names

    def getGroupNames(self, group_ids):
        names = dict()
        for chunk in self.chunks(group_ids):
            names |= self.getGroupNamesChunk(chunk)
        return names
        

    # def getGroupNames(self, groups):
    #     names = dict()
    #     for chunk in self.chunks(groups):
    #         names |= self.executeGroupNames(chunk)
    #     return names

    # def executeGroupNames(self, groups):
    #     assert len(groups) <= 25, "can't execute more than 25 requests per procedure"
    #     url = f"https://api.vk.com/method/execute.groupNames?access_token={self.access_token}&groups={','.join(list(map(str, groups)))}&v=5.131"
    #     resp = self.request(url)
    #     names = dict()
    #     for g in resp:  
    #         names[g["id"]] = (g["name"], g["screen_name"])
    #     return names

    def isRight(self, group_name):
        d = ("z", "патриот", "путин", "родина", "нац")
        for i in d:
            if i in group_name.lower():
                return True
        return False

    def checkRight(self, group_list):
        cnt = 0
        for group in group_list:
            if self.isRight(group):
                return True
        return False
