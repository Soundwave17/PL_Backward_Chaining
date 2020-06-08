from Connector import Connector
from Literal import Literal

class Node:

    def __init__(self, literal : Literal):
        self.literal = literal
        self.name= literal.name
        self.connectors = {}  # ORs

    def hasRequisite(self, node):
        for connector in self.connectors.values():
            if (connector.hasNode(node)):
                return True
        return False

    def addConnector(self, children):
        name = self.name + str(len(self.connectors))
        connector= Connector(self, name)
        for child in children :
            connector.addNode(child)
        self.connectors[name] = connector