import Node
from ANDORGraph import ANDORGraph
from KnowledgeBase import KnowledgeBase
from Literal import Literal

from timeit import default_timer as timer

def forwardChaining (KB : KnowledgeBase, query : Literal):
    start = timer()
    if (query not in KB.literals):
        raise Exception("Query cannot be found in KB's literals")

    #Creating count, a dictionary with the size of each literal's premise.
    count = {}
    for clause in KB.getStricts():
        count[clause.stringify()] = len(clause.body)
    #Creating inferred, a list of processed nodes
    inferred ={}
    for literal in KB.literals :
        inferred[literal.name] = False

    #Creating agenda, a list of true facts.
    agenda = []
    for fact in KB.getFacts():
        agenda.append(fact.head.name)
    if query.name in agenda:
        end = timer()
        duration = end - start
        return [True,[], duration]
    #Running Algorithm
    while (len(agenda) != 0):
        currentFact = agenda.pop()
        if(not inferred[currentFact]):
            inferred[currentFact] = True
            for c in KB.getStricts():
                C_body = [literal.name for literal in c.getBodyLiterals()]
                if (currentFact in C_body):
                    count[c.stringify()] -= 1
                    if (count[c.stringify()] == 0) :
                        if(c.head.name == query.name):
                            path=[]
                            for node in inferred:
                                if (inferred[node]):
                                    path.append(node)
                            path.append(query.name)
                            end = timer()
                            duration = end - start
                            return [True, path, duration]
                        else:
                            agenda.append(c.head.name)
    path=[]
    for node in inferred:
        if (inferred[node]):
            path.append(node)
    end = timer()
    duration = end - start
    return [False, path, duration]

def backwardChaining(KB : KnowledgeBase, graph : ANDORGraph, query : Literal):

    def dive(inferred : [], facts : [] , path : [], node : Node):
        inferred[node.name] = True #Node has been processed atleast once.
        if node.name in path and node.name not in facts: #Cycle exception
            return False
        else:
            if(node.name not in path):
                path.append(node.name)
        if node.name in facts: #Fact check
            return True
        for connector in node.connectors.values():
            connectedCheck=[]
            for connectedNode in connector.connectedNodes:
                connectedCheck.append(dive(inferred,facts, path, connectedNode))
            if (False not in connectedCheck):
                return True
        return False

    start = timer()
    if (query not in KB.literals):
        end = timer()
        raise Exception("Query cannot be found in KB's literals")

    inferred = {}
    for literal in KB.literals:
        inferred[literal.name] = False

    facts= []
    for fact in KB.getFacts():
        facts.append(fact.head.name)

    path=[]
    if (query.name in facts):
        end = timer()
        duration = end - start
        return [True,[],[query.name], duration]
    queryNode = graph.getNode(query.name)
    if(dive(inferred, facts, path, queryNode)):
        processedNodes=[]
        for node in inferred:
            if (inferred[node]):
                processedNodes.append(node)
        end = timer()
        duration = end - start
        return [True,processedNodes, path, duration]
    else:
        processedNodes = []
        for node in inferred:
            if (inferred[node]):
                processedNodes.append(node)
        end = timer()
        duration = end-start
        return [False, processedNodes, [], duration]