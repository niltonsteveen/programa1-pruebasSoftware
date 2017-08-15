import unittest

from linkedList import LinkedList
from linkedList import Node
from linkedList import myExc

class TestNode(unittest.TestCase):
    def setUp(self):
        self.node = Node()
    def testCreateNode(self):
        self.node.createNode(3, None)
        self.assertEqual(3, self.node.data)

class TestsLinkedList(unittest.TestCase):
    def setUp(self):
        self.linkedList = LinkedList()


if __name__ == '__main__':
    unittest.main()
