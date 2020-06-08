from InferenceMethods import backwardChaining, forwardChaining
from KnowledgeBase import createRandomHornKB

KB, goal, facts = createRandomHornKB(2, 7, 1, 0)
KB.printKB()
graph = KB.getANDORGraph()
graph.plotGraph(KB, [], "creation.png")

results =forwardChaining(KB, goal)
print(results[0])
graph.plotGraph(KB, results[1], "creation.png")
results =backwardChaining(KB,graph,goal)
print(results[0])
graph.plotGraph(KB, results[1], "creation.png")
