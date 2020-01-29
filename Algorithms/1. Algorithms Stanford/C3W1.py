#Greedy algorithm for minimizing weighted summ of completion time

"""
def score1(w, l):
    return w - l

def score2(w, l):
    return w/float(l)

def loadData(fName):
    with open(fName, 'r') as fileObj:
        lines = fileObj.readlines()
        numJobs = int(lines[0].strip())    # first line contains number of jobs
        jobList = [ (int(line.split()[0]), int(line.split()[1])) for line in lines[1:] ] 

    return jobList

def sortJobs(jobList, scoreFunc):
    scoreJobList = [ (w, l, scoreFunc(w, l)) for w, l in jobList ]
    scoreJobList.sort(key=lambda tup: tup[0], reverse=True)   # sort by weight first to resolve ties
    scoreJobList.sort(key=lambda tup: tup[2], reverse=True)   # sort by score function

    return scoreJobList

def sumCompletionTimes(sortedJobList):
    weightedSum = 0
    lengthSum = 0

    for job in sortedJobList:
        lengthSum += job[1]
        weightedSum += job[0] * lengthSum

    return weightedSum, lengthSum

def main(fName, scoreFunc):
    print("Loading data")
    jobList = loadData(fName)
    print("Computing scores for jobs and sorting")
    scoreJobList = sortJobs(jobList, scoreFunc)
    print("Computing weighted sum of completion times")
    weightedSum, lengthSum = sumCompletionTimes(scoreJobList)
    print("Weighted sum: {0}\nLength sum: {1}".format(weightedSum, lengthSum))

if __name__ == '__main__':
    main('jobs.txt', score1)

"""


#Prim's minimum spanning tree algorithm

def getGraph(fPath="edges.txt"):

    edgeList = []
    with open(fPath) as f:
        lines = f.readlines()
        numNodes, numEdges = [ int(el) for el in lines[0].split() ]
        for line in lines[1:]:
            node1, node2, edgeCost = [ int(el) for el in line.split() ]
            edgeList.append((node1, node2, edgeCost))

    return edgeList, numNodes, numEdges


def prim(edgeList, numNodes):
    """
    Run Prim's MST on graph in the form of edge list
    """

    X = set()  # set of explored nodes
    V = set(range(1, numNodes+1))   # set of unexplored nodes
    E = set()   # set of edges of MST
    totalCost = 0   # total sum of the edge costs of the MST

    start = 1
    X.add(start)
    V.remove(start)

    while len(V) is not 0:
        # look at all edges crossing the X and V sets
        lowestCost = float('inf')
        foundNodeX = None
        foundNodeV = None

        for edge in edgeList:
            if edge[0] in X and edge[1] in V:
                if edge[2] < lowestCost:
                    foundNodeX = edge[0]
                    foundNodeV = edge[1]
                    lowestCost = edge[2]
            elif edge[1] in X and edge[0] in V:
                if edge[2] < lowestCost:
                    foundNodeX = edge[1]
                    foundNodeV = edge[0]
                    lowestCost = edge[2]

        print("foundNodeX: {0}, foundNodeV: {1}".format(foundNodeX, foundNodeV))

        X.add(foundNodeV)
        V.remove(foundNodeV)
        E.add((foundNodeX, foundNodeV, lowestCost))
        totalCost += lowestCost

    return E, totalCost

if __name__ == '__main__':
    print("Computing MST...")
    edgeList, numNodes, numEdges = getGraph()
    E, totalCost = prim(edgeList, numNodes)

    print("Total cost: {}".format(totalCost))