import os

class ReadFile(object):
    def __init__(self):
        self.file=None
        self.muestra=[]
        self.filename = ""
    def readFile(self, filename):
        if not(os.path.exists(filename)):
            return False
        self.file = open(filename, 'r')
        for line in self.file.readlines():
            self.muestra.append(int(line))
        return True
    def onlyRead(self):
        return True if self.file.mode == 'r' else False
    def readFilename(self, readName):
        self.filename = readName()
        return
    def readName():
        return raw_input("What file do you want to read? ")
