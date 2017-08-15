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
    def testChangeLink(self):
        node2 = Node()
        self.node.changeLink(node2)
        self.assertEqual(node2, self.node.link)

class TestsLinkedList(unittest.TestCase):
    def setUp(self):
        self.linkedList = LinkedList()


if __name__ == '__main__':
    unittest.main()
