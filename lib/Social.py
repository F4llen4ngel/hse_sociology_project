from lib.Parser import Parser


class SocialAnalyzer:
    def __init__(self):
        self.parser = Parser()

    def searchCringe(self, groupList):
        pass

    def searchBase(self, groupList):
        pass
    
    def analyze(self, user_id):
        user_groups = self.parser.getUserGroups(user_id)
        user_cringe = self.searchCringe(user_groups)
        user_base = self.searchBase(user_groups)
        if user_base:
            return "Based"
        elif user_cringe:
            return "Cringe"
        else:
            return "amongus"