import os

class myExc(Exception): print "Exception! Your file contains non-numeric information"

class LinkedList(object):
    def __init__(self):
        nodeHead = Node()
    def createLinkedList(self):
        self.nodeHead = Node()
        self.nodeHead.createNode(0, None)
    def addNode(self, node):
        node1 = self.nodeHead
        node2 = None
        while node1 != None:
            node2 = node1
            node1 = node1.link
        node2.link = node
        self.nodeHead.data += 1
    
class Node(object):
    def __init__(self):
        data = None
        link = None
    def createNode(self, data, link):
        self.data = data
        self.link = link
    def changeLink(self, node):
        self.link = node