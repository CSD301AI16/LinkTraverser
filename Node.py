class Node(object):
    link: str
    inboundList = []
    outboundList = []

    def __init__(self, value, ibL=[], obL=[]):
        self.link = value
        for iblink in ibL:
            self.insertInbound(iblink)
        for oblink in obL:
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
        self.inboundList.append(node)

    def insertOutbound(self, node):
        self.outboundList.append(node)




