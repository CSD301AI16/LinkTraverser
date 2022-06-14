from getlink import LinkTraverser
from Graph import Graph
from Node import Node

url = "https://fptshop.com.vn/"

travser1 = LinkTraverser(rootURL = url, max = 23)
list = travser1.get_href_list()
oblist = []


transver = Graph(url)

##print(transver.rootNode)
for link in list:
    transver.rootNode.insertOutbound(Node(link, ibL=[transver.rootNode]))

for i in transver.summaryLinkList[url].outboundList:
    print(str(i))
