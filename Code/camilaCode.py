import os

class myExc(Exception): print "Exception! Your file contains non-numeric information"

class ReadFile(object):
    def __init__(self):
        self.file=None
        self.muestra=[]
    def readFile(self, filename):
        if not(os.path.exists(filename)):
            return False
        self.file = open(filename, 'r')
        try:
            for line in self.file.readlines():
                self.muestra.append(int(line))
        except myExc:
            raise myExc
            return
        return True
    def onlyRead(self):
        return True if self.file.mode == 'r' else False
    def readFilename(self, readName):
        return readName()
    def readName():
        return raw_input("What file do you want to read? ")
