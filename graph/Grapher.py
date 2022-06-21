import requests
from bs4 import BeautifulSoup
from queue import Queue
rootLink = "https://www.youtube.com/"


class Node:
    def __init__(self, link: str = None, inboundList: list = [], outboundList: list = []) -> None:
        self.link = link
        self.inboundList = inboundList
        self.outboundList = outboundList

    def getNumberOfInbound(self) -> int:
        if self.inboundList != None:
            return len(self.inboundList)
        else:
            return None

    def getNumberOfOutbound(self) -> int:
        if self.outboundList != None:
            return len(self.outboundList)
        else:
            return None

    def insertInbound(self, node):
        self.inboundList.append(node)

    def insertOutbound(self, node):
        self.outboundList.append(node)

    def findInbound(self, link: str):
        if not(self.inboundList is None):
            for i in self.inboundList:
                if i.link == link:
                    return False
            return True
        else:
            return False

    def findOutbound(self, link: str):
        if not(self.outboundList is None):
            for i in self.outboundList:
                if i.link == link:
                    return False
            return True
        else:
            return False


class Graph:
    def __init__(self, rootNode: Node = None, summaryLinkList: dict = {}, max_href: int = 50, maxNode: int = 1000) -> None:
        self.rootNode = rootNode
        self.summaryLinkList = summaryLinkList
        self.max_hrefs = max_href
        self.maxNode = maxNode

    def crawledLink(self, link: str) -> bool:
        if self.summaryLinkList is None:
            return False
        else:
            return (link in self.summaryLinkList)

    def insertNode(self, currentNode: Node, link: str) -> bool:
        if (self.crawledLink(link)):
            try:
                if not currentNode.findOutbound(link):
                    currentNode.insertOutbound(self.summaryLinkList[link])
                    self.summaryLinkList[link].insertInbound(currentNode)
                return False
            except:
                print(link)
        else:
            newNode = Node(link=link)
            self.summaryLinkList[link] = newNode
            currentNode.insertOutbound(newNode)
            newNode.insertInbound(currentNode)
            return True

    def getNodeByLink(self, link: str) -> Node:
        try:
            return self.summaryLinkList[link]
        except Exception as e:
            print(e)
            return None

    def get_href_list(self, link: str):
        page = requests.get(link)
        soup = BeautifulSoup(page.content, 'html.parser')
        href_list = []
        for a in soup.find_all('a'):
            href = a.get("href")
            if href is None:
                continue
            if not ('.com' in href or '.vn' in href):  # href is a subfolder in the webpage
                href = link + '/' + href
            href = href.rstrip('/')
            if href == link:
                continue
            if not self.isURLReachable(href):
                continue
            href_list.append(href)
            if len(href_list) >= self.max_hrefs:
                break
        return href_list

    def isURLReachable(self, url):
        try:
            page = requests.get(url)
            print("Valid URL. A Traverser object created.")

        except requests.exceptions.RequestException as err:
            print("URL {} is unreachable.".format(url))
            return False
            # raise err   # if not raising error here. An object with invalid URL will eventually cause exception later
        return True

    def BFS(self):
        queue = Queue(maxsize=10000)
        queue.put(self.rootNode.link)
        while (len(self.summaryLinkList) <= self.maxNode) and (not queue.empty()):
            currentLink = queue.get()
            linkHref = self.get_href_list(currentLink)
            for i in linkHref:
                notChecked = self.insertNode(
                    currentNode=self.summaryLinkList[currentLink], link=i)
                if notChecked:
                    queue.put(i)

    def empty(self):
        self.rootNode = None
        self.summaryLinkList = dict()

    def _insert_node_into_sorted_list(self, node: Node):
        i = 0
        while True:
            # print('Length of sorted list at iteration {}: {}'.format(i, len(self.sorted_list)))
            if i == len(self.sorted_list):
                self.sorted_list.append(node)
                return
            if node.getNumberOfInbound() > self.sorted_list[i].getNumberOfInbound():
                i += 1
                continue
            if node.getNumberOfInbound() == self.sorted_list[i].getNumberOfInbound():
                if node.getNumberOfOutbound > self.sorted_list[i].getNumberOfOutbound():
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

    def get_sorted_elements(self):
        return self.sorted_list


if __name__ == "__main__":
    root = Node(link=rootLink)
    graph = Graph(root, summaryLinkList={
                  rootLink: root}, max_href=2, maxNode=10)
    graph.BFS()
