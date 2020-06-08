import string
from ANDORGraph import ANDORGraph
from HornClause import HornClause, clauseEquals
from Literal import Literal
import random

class KnowledgeBase:

    def __init__(self):
        self.clauses = []
        self.literals = []

    def getSize(self):
        size = 0
        for clause in self.clauses:
            size += clause.getSize()
        return size

    def addClause(self,clause : HornClause):
        for c in self.clauses:
            if clauseEquals(c,clause):
                return
        self.clauses.append(clause)
        for literal in clause.getLiterals():
            if(not self.hasLiteral(literal)):
                self.literals.append(literal)

    def hasLiteral(self, literal):
        if(isinstance(literal,Literal)):
            for l in self.literals:
                if(literal.name == l.name):
                    return True
            return False
        elif(isinstance(literal, str)):
            for l in self.literals:
                if(literal == l.name):
                    return True
            return False
        else:
            raise Exception("Given parameter's type is not Literal or String")

    def getLiteral(self, name : str):
        if(self.hasLiteral(name)):
            for literal in self.literals:
                if (literal.name == name):
                    return literal
        else:
            return None

    def copyKB(self):
        newKB = KnowledgeBase()
        for clause in self.clauses:
            copyClause = clause.copy()
            newKB.addClause(copyClause)
        return newKB

    def getFacts(self):
        facts = []
        for clause in self.clauses:
            if (clause.isFact):
                facts.append(clause)
        return facts

    def getStricts(self):
        stricts =[]
        for clause in self.clauses:
            if (clause.isStrict):
                stricts.append(clause)
        return stricts

    def getANDORGraph(self):
        graph = ANDORGraph()
        for literal in self.literals:
            graph.addNode(literal)
        for clause in self.clauses:
            head = clause.head
            premise = clause.body
            if(len(premise) != 0):
                graph.connect(head,premise)
        return graph

    def printKB(self):
        print("Knowledge Base clauses: ")
        for clause in self.clauses:
            clause.printClause()
        print("__")

    def scramble(self):
        random.shuffle(self.clauses)
        random.shuffle(self.literals)

def createHornKB():
    KB = KnowledgeBase()
    reply = "Start"
    print("Welcome, please insert the knowledgebase, one Horn Clause at a time (example : 'A<=B,C,D,E' or simply 'G') "
          "and type 'Done' when you are ready to proceed:")
    while (reply != "Done"):
        print(">_ ", end='')
        reply = input()
        if (reply != "Done"):
            if "<=" in reply:
                strHead, unrefinedStrBody = reply.split("<=", 1)
                strBody = unrefinedStrBody.split(",")
                head = Literal(strHead)
                body= [Literal(v) for v in strBody]
                clause = HornClause(head, body)
            else:
                head = Literal(reply)
                clause = HornClause(head)
            KB.addClause(clause)
    return KB

def createRandomHornKB(branching: int, depth : int, clauseSize: int, noise : int):
    def createUniqueName(count : int, alphabet):
        if(count<=25):
            return alphabet[count]
        else:
            index = count % 25
            letter = alphabet[index]
            return createUniqueName(int((count - index)/25), alphabet) + letter

    def diveCreation(KB : KnowledgeBase, literal:Literal, branching:int, depth:int, clauseSize:int, literalSet, leaves, currentDepth:int, truth:bool, query: Literal):
        if((currentDepth+1) >= depth):
            if(truth):
                count = 0
                while count < branching:
                    body = []
                    while len(body) < clauseSize:
                        fact = leaves.pop()
                        factClause= HornClause(fact)
                        KB.addClause(factClause)
                        body.append(fact)
                    clause = HornClause(literal,body)
                    KB.addClause(clause)
                    count +=1
                return
            else:
                count = 0
                while count < branching:
                    body = []
                    while len(body) < clauseSize:
                        nonfact = leaves.pop()
                        body.append(nonfact)
                    clause = HornClause(literal, body)
                    KB.addClause(clause)
                    count += 1
                return
        else:
            count = 0
            while count < branching:
                if count == 0:
                    body = []
                    while len(body) < clauseSize:
                        body.append(literalSet.pop())
                    clause = HornClause(literal, body)
                    KB.addClause(clause)
                    for element in body:
                        diveCreation(KB, element, branching, depth, clauseSize, literalSet, leaves, currentDepth + 1, True, query)
                    count += 1
                else:
                    body=[]
                    while len(body) < clauseSize:
                        body.append(literalSet.pop())
                    clause = HornClause(literal, body)
                    KB.addClause(clause)
                    for element in body:
                        diveCreation(KB, element, branching, depth, clauseSize, literalSet, leaves, currentDepth + 1, False, query)
                    count +=1
            return

    def diveNoiseCreation(KB : KnowledgeBase, literal:Literal, branching:int, depth:int, clauseSize:int, literalSet, currentDepth:int, query : Literal):
        count = 0
        while count < branching:
            body = []
            while len(body) < clauseSize:
                body.append(literalSet.pop())
            clause = HornClause(literal, body)
            KB.addClause(clause)
            count += 1
            if currentDepth < depth:
                for element in body:
                    diveNoiseCreation(KB, element, branching, depth, clauseSize, literalSet, currentDepth + 1, query)
        return

    def climbNoiseCreation(KB:KnowledgeBase, literal:Literal, branching:int,literalSet, currentDepth:int):
        if currentDepth == 0:
            return
        count=0
        while count < branching:
            head = literalSet.pop()
            body=[]
            body.append(literal)
            clause= HornClause(head,body)
            climbNoiseCreation(KB, head, branching,literalSet, currentDepth -1)
            KB.addClause(clause)
            count += 1
        return

    #Creating random KB
    KB=KnowledgeBase()

    #Creating alphabet
    alphabet = list(string.ascii_uppercase)

    #Calculating parameters
    if depth == 1:
        truths =(branching * clauseSize)** (depth)
    else:
        truths = (branching * clauseSize)** (depth-1)
    elementsNumber = ((branching * clauseSize)**depth) + 1
    noiseElements = ((branching  * clauseSize)**depth)*noise + (noise*branching*depth*truths)
    elementsNumber = elementsNumber + noiseElements

    #Creating literals pool
    literalSet =[]
    count = 1
    while (count <= elementsNumber) :
        literalName= createUniqueName(count, alphabet)
        count = count +1
        literal = Literal(literalName)
        literalSet.append(literal)

    #selecting Goal
    goal = literalSet.pop()

    #selecting Facts
    leaves = []
    factsNumber= int(truths)
    while factsNumber != 0 :
        factsNumber -= 1
        fact = literalSet.pop()
        leaves.append(fact)

    copyLeaves= []
    for leaf in leaves:
        copyLeaves.append(leaf)

    diveCreation(KB, goal, branching, depth, clauseSize,literalSet,leaves,1, True, goal)

    if(noise !=0):
        count = 0
        while count < noise:
            diveNoiseCreation(KB, goal, branching,int(depth/2),clauseSize,literalSet,1, goal)
            count += 1

        for fact in copyLeaves:
            secondCount = 0
            while secondCount < noise:
                climbNoiseCreation(KB, fact, branching, literalSet, int(depth/2))
                secondCount += 1
    KB.scramble()
    return [KB, goal, KB.getFacts()]