
class Connector:
    def __init__(self, father, name : str):
        self.connectedNodes= [] #ANDs
        self.father = father
        self.name = name

    def addNode(self, node):
        if  (not self.hasNode(node)):
            self.connectedNodes.append(node)

    def hasNode(self, node):
        for connected in self.connectedNodes:
            if(connected.name == node.name):
                return True
        return False
