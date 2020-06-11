from InferenceMethods import forwardChaining, backwardChaining
from KnowledgeBase import KnowledgeBase
from Literal import Literal
from HornClause import HornClause

#Wumpus-Test : we want to demonstrate that, in a 3x2 world,  (2,2) contains a pit:

P11 = Literal("P11")
P12 = Literal("P22")
P21 = Literal("P21")
B11 = Literal("B11")
B12 = Literal("B12")
B21 = Literal("B21")
P22 = Literal("P22")
B22 = Literal("B22")
P31 = Literal("P31")
B32 = Literal("B32")

clauseP22 = HornClause(P22, [B21,B12])
clauseP11 = HornClause(P11,[B12,B21])
clauseP12 = HornClause(P12, [B11,B22])
clauseP21 = HornClause(P21, [B11,B22])
clauseB21 = HornClause(B21)
clauseB12 = HornClause(B12)
clauseB32 = HornClause(B32, [P22])
clauseP31 = HornClause(P31,[B21, B32])

KB = KnowledgeBase()
KB.addClause(clauseP11)
KB.addClause(clauseP12)
KB.addClause(clauseP21)
KB.addClause(clauseB21)
KB.addClause(clauseB12)
KB.addClause(clauseP22)
KB.addClause(clauseP31)
KB.addClause(clauseB32)


KB.printKB()
graph = KB.getANDORGraph()
graph.plotGraph(KB, [], "plots/ToyTest/WumpusTheoremProvingBefore.png")

query = KB.getLiteral("P22")

FC_results = forwardChaining(KB,query)
print("ForwardChaining resulted in: " + str(FC_results[0]))
graph.plotGraph(KB,FC_results[1], "plots/ToyTest/WumpusTheoremProvingFC_Processed.png")
BC_results = backwardChaining(KB,graph,query)
print("BackwardChaining resulted in: " + str(BC_results[0]))
graph.plotGraph(KB,BC_results[1], "plots/ToyTest/WumpusTheoremProvingBC_Processed.png")
if(BC_results[0]):
    print("With path: ", end='')
    counter = len(BC_results[2])
    for step in BC_results[2]:
        print(step, end='')
        counter -= 1
        if(counter != 0):
            print(",", end='')
    print("")

print("Forward_Chaining executed in: " + str(FC_results[2]) + " seconds")
print("Backward_Chaining executed in: " + str(BC_results[3]) + " seconds")
print("-----------------------------------------------------------------")


#West-Criminal Test
print("__________________________")
print("Beginning Criminal Test :")

American = Literal("American")
Criminal = Literal("Criminal")
Weapon= Literal("Weapon")
Missile = Literal("Missile")
Sells= Literal ("Sells")
Owns= Literal("Owns")
Hostile= Literal("Hostile")
Enemy= Literal("Enemy")

AmericanClause=HornClause(American)
MissileClause= HornClause(Missile)
OwnsClause= HornClause(Owns)
CriminalClause = HornClause(Criminal, [American, Weapon, Sells, Hostile])
WeaponClause= HornClause(Weapon, [Missile])
SellsClause= HornClause(Sells, [Missile, Owns])
EnemyClause= HornClause(Enemy)
HostileClause = HornClause(Hostile, [Enemy])

KB= KnowledgeBase()
KB.addClause(MissileClause)
KB.addClause(OwnsClause)
KB.addClause(CriminalClause)
KB.addClause(AmericanClause)
KB.addClause(WeaponClause)
KB.addClause(SellsClause)
KB.addClause(EnemyClause)
KB.addClause(HostileClause)

graph = KB.getANDORGraph()
graph.plotGraph(KB,[], "plots/ToyTest/CriminalTheoremProvingBefore.png")
KB.printKB()
query = KB.getLiteral("Criminal")

FC_results = forwardChaining(KB,query)
print("ForwardChaining resulted in: " + str(FC_results[0]))
graph.plotGraph(KB,FC_results[1], "plots/ToyTest/CriminalTheoremProvingFC_Processed.png")
BC_results = backwardChaining(KB,graph,query)
print("BackwardChaining resulted in: " + str(BC_results[0]))
graph.plotGraph(KB,BC_results[1], "plots/ToyTest/CriminalTheoremProvingBC_Processed.png")
if(BC_results[0]):
    print("With path: ", end='')
    counter = len(BC_results[2])
    for step in BC_results[2]:
        print(step, end='')
        counter -= 1
        if(counter != 0):
            print(",", end='')
    print("")

print("Forward_Chaining executed in: " + str(FC_results[2]) + " seconds")
print("Backward_Chaining executed in: " + str(BC_results[3]) + " seconds")
print("-----------------------------------------------------------------")