class ReadFile(object):
    def __init__(self):
        self.file=None
        self.muestra=[]
    def readFile(self, nameFile):
        self.file = open(nameFile, 'r')
        for line in self.file.readlines():
            self.muestra.append(int(line))
        print self.muestra
        return
    def onlyRead(self):
        return True if self.file.mode == 'r' else False