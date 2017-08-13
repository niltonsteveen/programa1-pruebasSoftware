import os

class ReadFile(object):
    def __init__(self):
        self.file=None
        self.muestra=[]
    def readFile(self, nameFile):
        if not(os.path.exists(nameFile)):
            return False
        self.file = open(nameFile, 'r')
        for line in self.file.readlines():
            self.muestra.append(int(line))
        print self.muestra
        return True
    def onlyRead(self):
        return True if self.file.mode == 'r' else False