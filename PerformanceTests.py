import pickle
from InferenceMethods import forwardChaining, backwardChaining
import matplotlib.pyplot as plt
import plotly
from plotly import figure_factory as ff

#Branching-increasing performance testing:
branchingLimit= 50
branching = 1
X=[]
FC_Time=[]
BC_Time=[]
time_table_data = [['Branching value', 'Knowledge Base Size', 'Forward Chaining Time', 'Backward Chaining Time']]

while branching <= branchingLimit:
    print(">_Branching Test with b = " + str(branching) + " ...")
    directory = "data/branchingData/" + str(branching) +"330/"
    KB = pickle.load(open(directory + "KB.p", "rb"))
    graph = KB.getANDORGraph()
    KB_size = KB.getSize()
    goal = KB.getLiteral(pickle.load(open(directory + "KBGoal.p", "rb")).name)

    X.append(KB_size)
    FC_results = forwardChaining(KB, goal)
    if(not FC_results[0]):
        raise Exception("Failed Testing at branching " + str(branching))
    BC_results = backwardChaining(KB, graph, goal)
    if (not BC_results[0]):
        raise Exception("Failed Testing at branching " + str(branching))

    FC_Time.append(round(FC_results[2], 3))
    BC_Time.append(round(BC_results[3],3))
    time_table_data.append([branching, KB_size, round(FC_results[2], 3), round(BC_results[3],3)])
    branching +=1

plt.plot(X, FC_Time)
plt.plot(X, BC_Time)
plt.legend(['Forward Chaining Time', 'Backward Chaining Time'])
plt.xlabel('Size')
plt.ylabel('Time in seconds')
plt.title('Branching Increasing Performance Test')
plt.savefig("plots/PerformanceTest/BranchingTest/BranchingTestPlot.png", format="PNG")
plt.show()

time_table = ff.create_table(time_table_data)
plotly.offline.plot(time_table, filename="results/Branching_Time_Table.html")


#ClauseSize-increasing performance testing:

clauseSizeLimit = 50
clauseSize = 1
X=[]
FC_Time=[]
BC_Time=[]

time_table_data = [['Clause Size value', 'Knowledge Base Size', 'Forward Chaining Time', 'Backward Chaining Time']]
while clauseSize <= clauseSizeLimit:
    print(">_ClauseSize Test with CS = " + str(clauseSize) + " ...")
    directory = "data/clauseSizeData/33" + str(clauseSize) +"0/"
    KB = pickle.load(open(directory + "KB.p", "rb"))
    graph = KB.getANDORGraph()
    KB_size = KB.getSize()
    goal = KB.getLiteral(pickle.load(open(directory + "KBGoal.p", "rb")).name)

    X.append(KB_size)
    FC_results = forwardChaining(KB, goal)
    if(not FC_results[0]):
        raise Exception("Failed Testing at clauseSize " + str(clauseSize))
    BC_results = backwardChaining(KB, graph, goal)
    if (not BC_results[0]):
        raise Exception("Failed Testing at clauseSize " + str(clauseSize))

    FC_Time.append(FC_results[2])
    BC_Time.append(BC_results[3])
    time_table_data.append([clauseSize, KB_size, round(FC_results[2], 3), round(BC_results[3],3)])
    clauseSize +=1

plt.plot(X, FC_Time)
plt.plot(X, BC_Time)
plt.legend(['Forward Chaining Time', 'Backward Chaining Time'])
plt.xlabel('Size')
plt.ylabel('Time in seconds')
plt.title('Clause Size Increasing Performance Test')
plt.savefig("plots/PerformanceTest/ClauseSizeTest/ClauseSizeTestPlot.png", format="PNG")
plt.show()

time_table = ff.create_table(time_table_data)
plotly.offline.plot(time_table, filename="results/ClauseSize_Time_Table.html")

#Noise-increasing performance testing:

noiseLimit = 50
noise =1
X=[]
FC_Time=[]
BC_Time=[]
time_table_data = [['Noise value', 'Knowledge Base Size', 'Forward Chaining Time', 'Backward Chaining Time']]

while noise <= noiseLimit:
    print(">_Noise Test with n = " + str(noise) + " ...")
    directory = "data/NoiseData/333" + str(noise) +"/"
    KB = pickle.load(open(directory + "KB.p", "rb"))
    graph = KB.getANDORGraph()
    KB_size = KB.getSize()
    goal = KB.getLiteral(pickle.load(open(directory + "KBGoal.p", "rb")).name)

    X.append(KB_size)
    FC_results = forwardChaining(KB, goal)
    if(not FC_results[0]):
        raise Exception("Failed Testing at noise " + str(noise))
    BC_results = backwardChaining(KB, graph, goal)
    if (not BC_results[0]):
        raise Exception("Failed Testing at noise " + str(noise))

    FC_Time.append(FC_results[2])
    BC_Time.append(BC_results[3])
    time_table_data.append([noise, KB_size,  round(FC_results[2], 3), round(BC_results[3],3)])
    noise +=1

plt.plot(X, FC_Time)
plt.plot(X, BC_Time)
plt.legend(['Forward Chaining Time', 'Backward Chaining Time'])
plt.xlabel('Size')
plt.ylabel('Time in seconds')
plt.title('Noise Increasing Performance Test')
plt.savefig("plots/PerformanceTest/NoiseTest/NoiseTestPlot.png", format="PNG")
plt.show()

time_table = ff.create_table(time_table_data)
plotly.offline.plot(time_table, filename="results/Noise_Time_Table.html")

#Depth-increasing performance testing:

depthLimit = 8
depth=1
X=[]
FC_Time=[]
BC_Time=[]

time_table_data = [['Depth value', 'Knowledge Base Size', 'Forward Chaining Time', 'Backward Chaining Time']]

while depth <= depthLimit:
    print(">_Depth Test with d = " + str(depth) + " ...")
    directory = "data/depthData/2" + str(depth) +"20/"
    KB = pickle.load(open(directory + "KB.p", "rb"))
    graph = KB.getANDORGraph()
    KB_size = KB.getSize()
    goal = KB.getLiteral(pickle.load(open(directory + "KBGoal.p", "rb")).name)

    X.append(KB_size)
    FC_results = forwardChaining(KB, goal)
    if(not FC_results[0]):
        raise Exception("Failed Testing at depth " + str(depth))
    BC_results = backwardChaining(KB, graph, goal)
    if (not BC_results[0]):
        raise Exception("Failed Testing at depth " + str(depth))

    FC_Time.append(FC_results[2])
    BC_Time.append(BC_results[3])
    time_table_data.append([depth, KB_size, round(FC_results[2], 3), round(BC_results[3],3)])
    depth +=1

plt.plot(X, FC_Time)
plt.plot(X, BC_Time)
plt.legend(['Forward Chaining Time', 'Backward Chaining Time'])
plt.xlabel('Size')
plt.ylabel('Time in seconds')
plt.title('Depth Increasing Performance Test')
plt.savefig("plots/PerformanceTest/DepthTest/DepthTestPlot.png", format="PNG")
plt.show()

time_table = ff.create_table(time_table_data)
plotly.offline.plot(time_table, filename="results/Depth_Time_Table.html")