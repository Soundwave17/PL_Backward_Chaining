from Literal import Literal
from Node import Node
import matplotlib.pyplot as plt
import networkx as nx

from Utilities import merge


class ANDORGraph:
    def __init__(self):
        self.nodes = {}

    def getNode(self, name : str):
        if(self.hasNode(name)):
            return self.nodes[name]
        else:
            raise Exception("Cannot find requested Node")

    def connect(self, head : Literal, premise: [Literal]):
        if(self.hasNode(head)):
            father = self.nodes[head.name]
        else:
            father = self.addNode(head)

        children = []
        for literal in premise:
            if(self.hasNode(literal)):
                children.append(self.nodes[literal.name])
            else:
                children.append(self.addNode(literal))

        father.addConnector(children)

    def addNode(self, literal : Literal):
        if(self.hasNode(literal)):
            raise Exception("Attempting to add redundant node.")
        else:
            node = Node(literal)
            self.nodes[literal.name] = node
            return node

    def hasNode(self, node):
        if(isinstance(node, Node)):
            for n in self.nodes.values():
                if(node.name == n.name):
                    return True
            return False
        elif(isinstance(node, str)):
            if(node in self.nodes):
                return True
            return False
        elif(isinstance(node, Literal)):
            if(node.name in self.nodes ):
                return True
            return False
        else:
            raise Exception("Parameter is not a Node, literal or string.")

    def getConnectors(self):
        connectors = {}
        for n in self.nodes.values():
            if(n.name in connectors):
                raise Exception("Adding duplicate connector")
            else:
                connectors[n.name] = n.connectors #returns connectors : {Node_str:{Connector_str:Connector}}
        return connectors

    def plotGraph(self, KB, inferred, FILEPATH):
        inferredCheck = False
        labelCheck = True
        base_size = 750
        if(len(inferred) != 0):
            inferredCheck = True
        if (len(self.nodes) > 50):
            labelCheck=False
            base_size = 50
        connectors = {}
        for value in self.nodes.values() :
            connectors = merge(connectors, value.connectors) #returns connectors : {Connector_str: Connector}

        edges =[]
        connectorSet= self.getConnectors() #: {Node_str:{Connector_str:Connector}}
        for nodeName in connectorSet:
            nodeConnectors = connectorSet[nodeName]
            for connectorName in nodeConnectors:
                edges.append((connectorName, nodeName))
                connector = connectorSet[nodeName][connectorName]
                for node in connector.connectedNodes:
                    edges.append((node.name,connectorName))

        if (len(edges) == 0):
            G = nx.DiGraph()
            facts = {}
            for n in self.nodes:
                for fact in KB.getFacts():
                    if fact.head.name == n:
                        facts[n] = self.nodes[n]
            if(inferredCheck):
                inferredNodes = {}
                for n in self.nodes:
                    if n not in facts:
                        if n in inferred:
                            inferredNodes[n] = self.nodes[n]
            normalNodes = {}
            for n in self.nodes:
                if n not in facts and n not in inferred:
                    normalNodes[n] = self.nodes[n]

            G.add_nodes_from(facts, Type="FACT")
            G.add_nodes_from(normalNodes, Type="NODE")
            if(inferredCheck):
                G.add_nodes_from(inferredNodes, Type="INFERRED")

            NODE_nodes = [n for (n, ty) in nx.get_node_attributes(G, 'Type').items() if ty == 'NODE']
            FACT_nodes = [n for (n, ty) in nx.get_node_attributes(G, 'Type').items() if ty == 'FACT']
            if(inferredCheck):
                INFERRED_nodes = [n for (n, ty) in nx.get_node_attributes(G, 'Type').items() if ty == 'INFERRED']

            pos = nx.circular_layout(G)
            plt.figure(3, figsize=(10, 10))
            if labelCheck:
                nx.draw_networkx_nodes(G, pos, nodelist=NODE_nodes, node_color="red", node_shape="o",
                                       node_size=[len(v) * base_size for v in NODE_nodes], with_labels=True)
                nx.draw_networkx_nodes(G, pos, nodelist=FACT_nodes, node_color="green", node_shape="o",
                                       node_size=[len(v) * base_size for v in FACT_nodes], with_labels=True)
                if (inferredCheck):
                    nx.draw_networkx_nodes(G, pos, nodelist=INFERRED_nodes, node_color="purple", node_shape="o",
                                       node_size=[len(v) * base_size for v in INFERRED_nodes], with_labels=True)
                nx.draw_networkx_edges(G, pos, edgelist=edges,arrowsize=25, node_size=base_size)

                nx.draw_networkx_labels(G, pos, font_color="white")
            else:
                nx.draw_networkx_nodes(G, pos, nodelist=NODE_nodes, node_color="red", node_shape="o",
                                       node_size=base_size, with_labels=True)
                nx.draw_networkx_nodes(G, pos, nodelist=FACT_nodes, node_color="green", node_shape="o",
                                       node_size=base_size, with_labels=True)
                if (inferredCheck):
                    nx.draw_networkx_nodes(G, pos, nodelist=INFERRED_nodes, node_color="purple", node_shape="o",
                                           node_size=base_size, with_labels=True)
                nx.draw_networkx_edges(G, pos, edgelist=edges, arrowsize=25, node_size=base_size)
            plt.savefig(FILEPATH, format="PNG")
            plt.show()

        else:
            G = nx.DiGraph()

            facts = {}
            for n in self.nodes:
                for fact in KB.getFacts():
                    if fact.head.name == n:
                        facts[n] = self.nodes[n]
            if(inferredCheck):
                inferredNodes = {}
                for n in self.nodes:
                    if n not in facts:
                        if n in inferred:
                            inferredNodes[n] = self.nodes[n]
            normalNodes = {}
            for n in self.nodes:
                if n not in facts and n not in inferred:
                    normalNodes[n] = self.nodes[n]

            G.add_nodes_from(facts, Type="FACT")
            G.add_nodes_from(normalNodes, Type="NODE")
            G.add_nodes_from(connectors, Type="CONNECTOR")
            if (inferredCheck):
                G.add_nodes_from(inferredNodes, Type="INFERRED")
            G.add_edges_from(edges)

            NODE_nodes = [n for (n, ty) in nx.get_node_attributes(G, 'Type').items() if ty == 'NODE']
            CONNECTOR_nodes = [n for (n, ty) in nx.get_node_attributes(G, 'Type').items() if ty == 'CONNECTOR']
            FACT_nodes =[n for (n, ty) in nx.get_node_attributes(G, 'Type').items() if ty == 'FACT']
            if (inferredCheck):
                INFERRED_nodes = [n for (n, ty) in nx.get_node_attributes(G, 'Type').items() if ty == 'INFERRED']

            pos = nx.spring_layout(G)
            plt.figure(3, figsize=(10, 10))
            if labelCheck:
                nx.draw_networkx_nodes(G, pos, nodelist=NODE_nodes, node_color="red", node_shape="o",
                                       node_size=[len(v) * base_size for v in NODE_nodes], with_labels=True)
                nx.draw_networkx_nodes(G, pos, nodelist=CONNECTOR_nodes, node_color="blue", node_shape="s",
                                       node_size=[len(v) * base_size for v in CONNECTOR_nodes], with_labels=True)
                nx.draw_networkx_nodes(G, pos, nodelist=FACT_nodes, node_color="green", node_shape="o",
                                       node_size=[len(v) * base_size for v in FACT_nodes], with_labels=True)
                if (inferredCheck):
                    nx.draw_networkx_nodes(G, pos, nodelist=INFERRED_nodes, node_color="purple", node_shape="o",
                                           node_size=[len(v) * base_size for v in INFERRED_nodes], with_labels=True)
                nx.draw_networkx_edges(G, pos, edgelist=edges, arrowsize=25, node_size=base_size)

                nx.draw_networkx_labels(G, pos, font_color="white")
            else:
                nx.draw_networkx_nodes(G, pos, nodelist=NODE_nodes, node_color="red", node_shape="o",
                                       node_size=base_size, with_labels=True)
                nx.draw_networkx_nodes(G, pos, nodelist=CONNECTOR_nodes, node_color="blue", node_shape="s",
                                       node_size=base_size, with_labels=True)
                nx.draw_networkx_nodes(G, pos, nodelist=FACT_nodes, node_color="green", node_shape="o",
                                       node_size=base_size, with_labels=True)
                if (inferredCheck):
                    nx.draw_networkx_nodes(G, pos, nodelist=INFERRED_nodes, node_color="purple", node_shape="o",
                                           node_size=base_size, with_labels=True)
                nx.draw_networkx_edges(G, pos, edgelist=edges, arrowsize=25, node_size=base_size)

            plt.savefig(FILEPATH, format="PNG")
            plt.show()

