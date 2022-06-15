from Node import Node


class Graph(object):
    rootNode: Node
    summaryLinkList = dict()
    size = 0

    def __init__(self, link: str, ibL=[], obL=[]):
        self.rootNode = Node(link)
        self.rootNode.inboundList = []
        self.rootNode.outboundList = []
        for iblink in ibL:
            if not self.getNode(iblink):
                curr = Node(iblink, obL=[self.rootNode])
                self.rootNode.insertInbound(curr)
                self.insertNode(curr)
        for oblink in obL:
            if not self.getNode(oblink):
                curr = Node(oblink, ibL=[self.rootNode])
                self.rootNode.insertOutbound(curr)
                self.insertNode(curr)
        self.summaryLinkList[link] = self.rootNode
        return

    def insertNode(self, node: Node, ibL=[], obL=[]):
        self.summaryLinkList[node.link] = node
        for iblink in ibL:
            if not self.getNode(iblink):
                curr = Node(iblink, obL=[self.rootNode])
                self.rootNode.insertInbound(curr)
                self.insertNode(curr)
        for oblink in obL:
            if not self.getNode(oblink):
                curr = Node(oblink, ibL=[self.rootNode])
                self.rootNode.insertOutbound(curr)
                self.insertNode(curr)
        return node

    def getRoot(self):
        return self.rootNode

    def setRoot(self, link: str):
        self.rootNode.link = link

    def getNode(self, link: str):
        return self.BFS(link)

    def isExist(self, link: str):
        if self.getNode(link):
            return True
        else:
            return False

    def BFS(self, link):
        visited = [self.rootNode]
        queue = [self.rootNode]

        while queue:
            curr = queue.pop(0)
            if curr.link == link:
                return curr
            for i in self.rootNode.outboundList:
                if i not in visited:
                    queue.append(i)
                    visited.append(i)
        return None


    def printBFT(self):
        visited = [self.rootNode]
        queue = [self.rootNode]

        while queue:
            curr = queue.pop(0)
            print (str(curr), end = " ")
            for i in self.rootNode.outboundList:
                if i not in visited:
                    queue.append(i)
                    visited.append(i)
        return None