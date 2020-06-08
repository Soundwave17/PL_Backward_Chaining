from Literal import Literal

class HornClause:

    def __init__(self, head : Literal, body = None):
        if (body is None or len(body) == 0) :
            self.head = head
            self.body = []
            self.isFact = True
            self.isStrict = False
        else:
            if(not self.hasValidBody(body)):
                raise Exception("Clause is not valid. Body has redundant literals")
            if(not self.isValidClause(head,body)):
                raise Exception("Clause is not valid, head is contained in the body.")
            self.head = head
            self.body = body
            self.isFact = False
            self.isStrict = True

    def getSize(self):
        return 1 + len(self.body)

    def getLiterals(self):
        literals = []
        literals.append(self.head)
        for literal in self.body:
            literals.append(literal)
        return literals

    def getBodyLiterals(self):
        literals = []
        for literal in self.body:
            literals.append(literal)
        return literals

    def stringify(self):
        if (self.isFact):
            return str(self.head.name)
        elif (self.isStrict):
            string = str(self.head.name + "<=")
            count = len(self.body)
            for literal in self.body:
                string = string + str(literal.name)
                count -= 1
                if (count != 0):
                    string = string + str(",")
            return string

    def printClause(self):
        if(self.isFact):
            print(":: "  + self.head.name,end='')
        elif(self.isStrict):
            print(":: " +self.head.name + " <= ", end='')
            count = len(self.body)
            for literal in self.body:
                print(literal.name, end='')
                count -=1
                if(count != 0):
                    print(",", end='')
        print("")

    def copy(self):
        copyHead = self.head.copy()
        copyBody=[]
        for literal in self.body:
            copyLiteral= literal.copy()
            copyBody.append(copyLiteral)
        copyClause = HornClause(copyHead,copyBody)
        return copyClause

    def isValidClause(self, head : Literal , body : [Literal]):
        for literal in body:
            if (head.name == literal.name):
                return False
        return True

    def hasValidBody(self, body : [Literal]):
        literals =[]
        for literal in body:
            if (literal.name in literals):
                return False
            else:
                literals.append(literal.name)
        return True

def clauseEquals(A : HornClause, B : HornClause):
    if (A.head.name == B.head.name):
        A_body = []
        B_body = []

        for literal in A.body:
            A_body.append(literal.name)
        for literal in B.body:
            B_body.append(literal.name)
        if len(A_body) != len(B_body):
            return False
        for name in A_body:
            if (name not in B_body) :
                return False
        return True
    else:
        return False
