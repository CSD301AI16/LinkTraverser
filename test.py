from getlink import LinkTraverser
from Graph import Graph
from Node import Node

url = "https://fptshop.com.vn/"

travser1 = LinkTraverser(rootURL = url, max= 50)
outboundlist = travser1.get_href_list()


transver = Graph(url, obL=outboundlist)
print(transver.summaryLinkList)