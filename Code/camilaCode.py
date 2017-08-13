import os

class ReadFile(object):
    def __init__(self):
        self.file=None
        self.muestra=[]
    def readFile(self, filename):
        if not(os.path.exists(filename)):
            return False
        self.file = open(filename, 'r')
        for line in self.file.readlines():
            self.muestra.append(int(line))
        print self.muestra
        return True
    def onlyRead(self):
        return True if self.file.mode == 'r' else False