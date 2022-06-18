from graph.Node import Node


class Graph(object):
    rootNode: Node
    summaryLinkList = dict()
    size = 0

    def __init__(self, link: str, ibL=[], obL=[]):
        self.rootNode = Node(link)
        self.rootNode.inboundList = []
        self.rootNode.outboundList = []
        self.insertNode(self.rootNode, ibL, obL)
        return None

    def insertNode(self, node: Node, ibL=[], obL=[]):
        self.summaryLinkList[node.link] = node
        for iblink in ibL:
            if not self.isExist(str(iblink)):
                curr = Node(iblink)
            else:
                curr = self.getNode(iblink)
            curr.insertOutbound(node)
            node.insertInbound(curr)
            self.insertNode(curr)
        for oblink in obL:
            if not self.isExist(oblink):
                curr = Node(oblink)
            else:
                curr = self.getNode(oblink)
            curr.insertInbound(node)
            node.insertOutbound(curr)
            self.insertNode(curr)
        return node

    def insertNodeByLink(self, link: str, ibL=[], obL=[]):
        return self.insertNode(Node(link), ibL, obL)

    def getRoot(self):
        return self.rootNode

    def setRoot(self, link: str):
        self.rootNode.link = link

    def getNode(self, link: str):
        return self.BFS(link)

    def isExist(self, link: str):
        if link in self.summaryLinkList.keys():
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
            for i in curr.outboundList:
                if i not in visited:
                    queue.append(i)
                    visited.append(i)
        return None

    def printBFT(self):
        visited = [self.rootNode]
        queue = [self.rootNode]

        while queue:
            curr = queue.pop(0)
            print(str(curr), end=" ")
            for i in curr.outboundList:
                if i not in visited:
                    queue.append(i)
                    visited.append(i)
        return None

    def _insert_node_into_sorted_list(self, node: Node):
        i = 0
        while True:
            # print('Length of sorted list at iteration {}: {}'.format(i, len(self.sorted_list)))
            if i == len(self.sorted_list):
                self.sorted_list.append(node)
                return
            if node.getNumberOfInBound() > self.sorted_list[i].getNumberOfInBound():
                i += 1
                continue
            if node.getNumberOfInBound() == self.sorted_list[i].getNumberOfInBound():
                if node.getNumberOfOutBound() > self.sorted_list[i].getNumberOfOutBound():
                    i += 1
                    continue
                self.sorted_list.insert(i, node)
                return
            self.sorted_list.insert(i, node)
            return

    def sort(self):
        self.sorted_list = []
        visited = [self.rootNode]
        queue = [self.rootNode]

        while queue:
            curr_node = queue.pop(0)
            self._insert_node_into_sorted_list(curr_node)
            for node in curr_node.outboundList:
                if node not in visited:
                    queue.append(node)
                    visited.append(node)

    def print_sorted_list(self):
        print(*self.sorted_list, sep='\n')
        print('{} elements in the sorted list'.format(len(self.sorted_list)))

    def empty(self):
        self.rootNode = None
        self.summaryLinkList = dict()
