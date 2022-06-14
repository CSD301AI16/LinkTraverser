import Node


class Graph(object):
    rootNode: Node = None
    summaryLinkList: dict()

    def __init__(self, link: str):
        self.rootNode.link = link
        self.rootNode.inboundList = list
        self.rootNode.outboundList = list
        self.summaryLinkList[link] = self.rootNode
        return

    def insertNode(self, link: str, ibL: list, obL: list):
        exist = self.getNodebyLink(link)
        if exist:
            print("Node existed")
        else:
            newNode = Node(link)
            for iblink in ibL:
                curribNode = self.getNodebyLink(str(iblink))
                if curribNode is None:
                    curribNode = self.insertNode(str(iblink), None, [newNode])
                else:
                    curribNode.insertOutbound(newNode)
                newNode.insertInbound(curribNode)

            for oblink in obL:
                currobNode = self.getNodebyLink(str(oblink))
                if currobNode is None:
                    currobNode = self.insertNode(str(oblink), [newNode], None)
                else:
                    currobNode.insertInbound(newNode)
                newNode.insertOutbound(currobNode)
            self.summaryLinkList[link] = newNode
        return newNode

    def insertNode(self, link: str):
        return self.insertNode(link=link, ibL=None, obL=None)

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
