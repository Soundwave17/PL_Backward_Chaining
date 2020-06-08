import os
import pickle
from KnowledgeBase import createRandomHornKB

branchingLimit=50
branching =1
while branching <= branchingLimit:
    print("branching " + str(branching))
    directory="data/branchingData/"+ str(branching) +"330/"
    os.makedirs(os.path.dirname(directory), exist_ok=True)

    KB, goal, facts = createRandomHornKB(branching,3,3,0)
    pickle.dump(KB ,open(directory + "KB.p", "wb"))
    pickle.dump(goal ,open(directory + "KBGoal.p","wb"))
    pickle.dump(facts, open (directory + "KBFacts.p","wb"))
    branching +=1


depthLimit= 8
depth=1
while depth <= depthLimit:
    print("depth " + str(depth))
    directory="data/depthData/"+ "2" +str(depth) +"20/"
    os.makedirs(os.path.dirname(directory), exist_ok=True)

    KB, goal, facts = createRandomHornKB(2,depth,2,0)
    pickle.dump(KB ,open(directory + "KB.p", "wb"))
    pickle.dump(goal ,open(directory + "KBGoal.p","wb"))
    pickle.dump(facts, open (directory + "KBFacts.p","wb"))
    depth +=1

clauseSizeLimit= 50
clauseSize= 1
while clauseSize <= clauseSizeLimit:
    print("clauseSize " + str(clauseSize))
    directory = "data/clauseSizeData/" + "33" + str(clauseSize) + "0/"
    os.makedirs(os.path.dirname(directory), exist_ok=True)

    KB, goal, facts = createRandomHornKB(3,3,clauseSize, 0)
    pickle.dump(KB, open(directory + "KB.p", "wb"))
    pickle.dump(goal, open(directory + "KBGoal.p", "wb"))
    pickle.dump(facts, open(directory + "KBFacts.p", "wb"))
    clauseSize += 1

noiseLimit=50
noise =1
while noise <= noiseLimit:
    print("noise " + str(noise))
    directory = "data/NoiseData/" + "333" + str(noise) +"/"
    os.makedirs(os.path.dirname(directory), exist_ok=True)

    KB, goal, facts = createRandomHornKB(3,3,3, noise)
    pickle.dump(KB, open(directory + "KB.p", "wb"))
    pickle.dump(goal, open(directory + "KBGoal.p", "wb"))
    pickle.dump(facts, open(directory + "KBFacts.p", "wb"))
    noise += 1