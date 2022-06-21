import requests
from bs4 import BeautifulSoup
from queue import Queue
from urllib.parse import urlparse, parse_qsl, unquote_plus
rootLink="https://www.youtube.com/"

class Node:
    def __init__(self,link:str=None,inboundList=None,outboundList=None) -> None:
        if inboundList==None: 
            inboundList=[]
        if outboundList==None: 
            outboundList=[]
        self.link=link
        self.inboundList=inboundList
        self.outboundList=outboundList
    def getNumberOfInbound(self)->int:
        if self.inboundList!=None:
            return len(self.inboundList)
        else:   
            return None
    def getNumberOfOutbound(self)->int:
        if self.outboundList!=None:
            return len(self.outboundList)
        else:   
            return None
    # each node have an inbound list to store nodes that link into it, this method will
    # this method insert a node to that list
    def insertInbound(self,node):
        self.inboundList.append(node)
    # like inbound list, but this is for outbound
    def insertOutbound(self,node):
        self.outboundList.append(node)
    # return whether this link is not in the Inbound list or else
    def findInbound(self,link:str):
        if not(self.inboundList is None):
            for i in self.inboundList:
                if i.link==link:
                    return False
            return True
        else:
            return False
    # return whether this link is not in the outbound list or else
    def findOutbound(self,link:str):
        if not(self.outboundList is None):
            for i in self.outboundList:
                if i.link==link:
                    return False
            return True
        else:
            return False
#def get_simulator(path:str)->
class Graph:
    def __init__(self,rootNode:Node=None,summaryLinkList:dict=None,max_href:int=50,maxNode:int=1000) -> None:
        if summaryLinkList==None:
            summaryLinkList={}
        self.rootNode=rootNode
        self.summaryLinkList=summaryLinkList
        self.max_hrefs=max_href
        self.maxNode=maxNode
    # return if the link is crawled or not
    def crawledLink(self,link:str)->bool:
        if self.summaryLinkList is None:
            return False
        else:
            return (link in self.summaryLinkList)
    # insert a link, if link not existed then return true, else return false.
    # note: even when existed but if the connection is new (new mean not violate the rule two outbound same or two inbound same)
    #       then the node is still be inserted.
    def insertNode(self,currentNode:Node,link:str)->bool:
        if (Url(currentNode.link)==Url(link)):
            return False
        if (self.crawledLink(link)):
            try:
                if not currentNode.findOutbound(link):
                    currentNode.insertOutbound(self.summaryLinkList[link])
                    self.summaryLinkList[link].insertInbound(currentNode)
                return False
            except:
                print(link)
        else:
            newNode=Node(link=link)
            self.summaryLinkList[link]=newNode
            currentNode.insertOutbound(newNode)
            newNode.insertInbound(currentNode)
            return True
    def getNodeByLink(self,link:str)->Node:
        try:
            return self.summaryLinkList[link]
        except Exception as e:
            print(e)
            return None
    def get_href_list(self,link:str):
        page = requests.get(link)
        soup = BeautifulSoup(page.content, 'html.parser')
        href_list = []
        for a in soup.find_all('a'):
            href = a.get("href")
            if href is None:
                continue
            if not ('.com' in href or '.vn' in href):           ## href is a subfolder in the webpage
                href = link + '/' + href
            href = href.rstrip('/')
            if href == link:
                continue
            if not self.isURLReachable(href):
                continue
            if (Url(href)==Url(link)):
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
    # using breadth first search to create the graph
    def BFS(self):
        queue=Queue(maxsize = 10000)
        queue.put(self.rootNode.link)
        while (len(self.summaryLinkList)<=self.maxNode)and(not queue.empty()):
            currentLink=queue.get()
            linkHref=self.get_href_list(currentLink)
            for i in linkHref:
                notChecked=self.insertNode(currentNode=self.summaryLinkList[currentLink],link=i)
                if notChecked:
                    queue.put(i)
class Url(object):
    '''A url object that can be compared with other url orbjects
    without regard to the vagaries of encoding, escaping, and ordering
    of parameters in query strings.'''

    def __init__(self, url):
        url=url.rstrip('/')
        parts = urlparse(url)
        _query = frozenset(parse_qsl(parts.query))
        _path = unquote_plus(parts.path)
        parts = parts._replace(query=_query, path=_path)
        self.parts = parts

    def __eq__(self, other):
        return self.parts == other.parts

    def __hash__(self):
        return hash(self.parts)
# make a root node
root=Node(link=rootLink)
# the summaryLinkList will have only the root node at first with root node's link as key,
# max_href= max number of link each node can point to
# maxNode= max number of node this graph can have 
from os.path import exists
def get_link_list(path:str)->list:
    if not exists(path):
        return None
    file_handle=open(path,"r")
    result=[]
    for i in file_handle:
        result.append(i)
    return result
graph=Graph(root,summaryLinkList={rootLink:root},max_href=5,maxNode=10)
# use BFS to make graph
graph.BFS()
#test git




            

