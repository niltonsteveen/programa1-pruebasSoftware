class ReadFile(object):
    def __init__(self):
        self.file=None
    def readFile(self, nameFile):
        self.file = open(nameFile, 'r')
        return
    def onlyRead(self):
        return True if self.file.mode == 'r' else False