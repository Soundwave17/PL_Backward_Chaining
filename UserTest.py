from KnowledgeBase import createHornKB
from InferenceMethods import forwardChaining
from InferenceMethods import backwardChaining


KB  = createHornKB()
KB.printKB()
graph = KB.getANDORGraph()
graph.plotGraph(KB,[], "plots/UserTest/beforeProcessing.png")
query = KB.getLiteral(input("Please input the query to demonstrate: "))

FC_results = forwardChaining(KB,query)
print("ForwardChaining resulted in: " + str(FC_results[0]))
graph.plotGraph(KB,FC_results[1], "plots/UserTest/FC_Processed.png")
BC_results = backwardChaining(KB,graph,query)
print("BackwardChaining resulted in: " + str(BC_results[0]))
graph.plotGraph(KB,BC_results[1], "plots/UserTest/BC_Processed.png")
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