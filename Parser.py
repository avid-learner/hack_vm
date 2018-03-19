
from pyparsing import Literal, CaselessLiteral, Word, OneOrMore, ZeroOrMore, \
Forward, NotAny, delimitedList, oneOf, Group, Optional, Combine, alphas, nums, restOfLine, cStyleComment, \
alphanums, printables, empty, quotedString, ParseException, ParseResults, Keyword, cppStyleComment, FollowedBy, \
ParserElement

segments = ["constant", "argument", "this", "that", "temp", "local", "static", "pointer"]
commands = ["add", "sub", "and", "neg", "eq", "gt", "lt", "or", "not"]

class MemoryCommand:
    def __init__(self, direction, segment, value):
        self.direction = direction
        self.segment = segment
        self.value = value
        self.isConstant = self.segment == "constant"

class Command:
    def __init__(self, name):
        self.name = name

class Parser:
    def __init__(self):
        self.number = Word(nums)
        ParserElement.setDefaultWhitespaceChars('\n\t\r ')
        self.comment = cppStyleComment
        self.segment = self.ListKeywords(segments)
        self.pushpop = ((Keyword("push") | Keyword("pop")) + self.segment + self.number).setParseAction(lambda s,l,t: self.GotPushPop(t))
        self.command = self.ListKeywords(commands).setParseAction(lambda s,l,t: self.GotCommand(t))
        self.line =  (self.command | self.pushpop  + Optional(self.comment)) | self.comment
        self.lines = ZeroOrMore(self.line)
        self.commands = []

    def GotPushPop(self, t):
        #print(t)
        self.commands.append(MemoryCommand(t[0] == "push", t[1], t[2]))

    def GotCommand(self, t):
        #print(t)
        self.commands.append(Command(t[0]))

    def ListKeywords(self, keywordList):
        parser = Keyword(keywordList[0])
        for key in keywordList[1:]:
            parser = parser | Keyword(key)
        return parser

    def ParseLine(self, line):
        return self.line.parseString(line)

    def ParseFile(self, file):
        self.lines.parseFile(file)
        return self.commands
