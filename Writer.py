import Parser
import jinja2


class AssemblerWriter:
    def __init__(self, fileName):
        self.file = open(fileName, "w")
        self.labelNumber = 0

    def MakeNewName(self, prefix, index):
        return prefix + str(index)

    def MakeNewLabel(self):
        result = self.MakeNewName("Label", self.labelNumber)
        self.labelNumber += 1
        return result

    def MakeNewVariable(self):
        result = self.MakeNewName("Variable", self.labelNumber)
        self.labelNumber += 1
        return result

    def Write(self, commands):
        for command in commands:
            self.WriteCommand(command)

    def WriteCommand(self, command):
        pass
