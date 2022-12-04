from lib.Parser import Parser

parser = Parser()
miem_members = list(set(parser.getGroupMembers(20122181)))
print(len(miem_members))
print(miem_members[-100:])