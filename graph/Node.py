class Node(object):
    link: str
    inboundList = []
    outboundList = []

    def __init__(self, value, ibL=[], obL=[]):
        self.link = value
        self.inboundList = []
        self.outboundList = []
        for iblink in ibL:
            if iblink not in self.inboundList:
                self.insertInbound(iblink)
        for oblink in obL:
            if oblink not in self.outboundList:
                self.insertOutbound(oblink)

#   def __init__(self, value):
#        self.link = value

    def __str__(self):
        return self.link

    def getNumberOfInBound(self):
        return len(self.inboundList)

    def getNumberOfOutBound(self):
        return len(self.outboundList)

    def insertInbound(self, node):
        if node not in self.inboundList:
            self.inboundList.append(node)

    def insertOutbound(self, node):
        if node not in self.outboundList:
            self.outboundList.append(node)




