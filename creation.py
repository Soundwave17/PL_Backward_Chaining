from InferenceMethods import backwardChaining, forwardChaining
from KnowledgeBase import createRandomHornKB

#Warning: using high value parameters will cause a MemoryError Exception to be thrown.
KB, goal, facts = createRandomHornKB(3, 3, 3, 1) #Parameters in order : Branching, Depth, Clause Size and Noise.
plotBeforeProcessing = True
plotProcessed = True

KB.printKB()
graph = KB.getANDORGraph()

if plotBeforeProcessing:
    graph.plotGraph(KB, [], "creation.png")

results =forwardChaining(KB, goal)
print(results[0])
if plotProcessed:
    graph.plotGraph(KB, results[1], "creation.png")
results =backwardChaining(KB,graph,goal)
print(results[0])
if plotProcessed:
   graph.plotGraph(KB, results[1], "creation.png")
