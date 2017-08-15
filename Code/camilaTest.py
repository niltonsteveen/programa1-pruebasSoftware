import unittest

from camilaCode import ReadFile
#from camilaCode import myExc

class TestsRead(unittest.TestCase):
    def setUp(self):
        self.read = ReadFile()
    def testReadFile(self):
        self.read.readFile("Code/numeros.txt")
        self.assertNotEqual(None, self.read.file)
    def testOnlyRead(self):
        self.read.readFile("Code/numeros.txt")
        self.assertTrue(self.read.onlyRead())
    def testReadNumbers(self):
        self.read.readFile("Code/numeros.txt")
        self.assertEqual([1,4,5,7,9],self.read.muestra)
    def testFileNoExist(self):
        response = self.read.readFile("Code/numerosx.txt")
        self.assertFalse(response)
    def testReadFileForConsole(self):
        output = self.read.readFilename(lambda: "Code/numbers.txt")
        self.assertEqual("Code/numbers.txt", output)
    def testReadFilenameAndFile(self):
        output = self.read.readFilename(lambda: "Code/numeros.txt")
        self.read.readFile(output)
        self.assertNotEqual(None, self.read.file)
   # def testReadNotNumbers(self):
    #    self.assertRaises(myExc)
if __name__ == '__main__':
    unittest.main()
