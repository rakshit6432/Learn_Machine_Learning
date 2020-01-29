#the clustering algorithm from lecture for computing a max-spacing k-clustering

"""
import unionfind as uf
from collections import deque

def getGraph(fPath="clustering1.txt"):

    edgeList = []
    with open(fPath) as f:
        lines = f.readlines()
        numNodes = int(lines[0])
        for line in lines[1:]:
            node1, node2, edgeCost = [ int(el) for el in line.split() ]
            edgeList.append((node1, node2, edgeCost))

    return edgeList, numNodes

def kclustering(k, edgeList, numNodes):
    
    # sort edges by their weights ascending, then select in this
    # order
    edgeList.sort(key=lambda tup: tup[2])
    edgeDeque = deque(edgeList)
    ufStruct = uf.UnionFind(list(range(1, numNodes+1))) # for 1-based

    while (ufStruct.totalComponents > k):
        # select cheapest edge that does not create cycles
        candidate = edgeDeque.popleft()
        ufStruct.union(candidate[0], candidate[1])

    # max spacing is the smallest unused edge
    while edgeDeque:
        maxSpacingEdge = edgeDeque.popleft()
        if ufStruct.find(maxSpacingEdge[0]) != \
                                    ufStruct.find(maxSpacingEdge[1]):
            break

    return maxSpacingEdge


if __name__ == '__main__':
    edgeList, numNodes = getGraph("clustering1.txt")
    k = 4
    maxSpacingEdge = kclustering(k, edgeList, numNodes)
    
    print("{}-clustering max spacing: {}".format(k, maxSpacingEdge[2]))

"""

#clustering algorithm from lecture, but on a MUCH bigger graph

import unionfind as uf
from itertools import izip, combinations

def getGraph(fPath="clustering_big.txt"):

    with open(fPath) as f:
        lines = f.readlines()
        numNodes, labelBits = map(int, lines[0].split())
        nodeList = []

        for line in lines[1:]:
            # trim '\n' by omitting last 2 characters
            node = "".join([ el for el in line if el is not " "])[:-1]
            nodeList.append(node)

    return nodeList, labelBits


def hammingDistance(node1, node2):
    assert len(node1) == len(node2)

    return sum(c1 != c2 for c1, c2 in izip(node1, node2))

def calculateMasks(bitsLabel=24):
    """
    Create swap masks in the form tuples with numbers
    indicating which bits to swap.
    """

    swapMasks1 = [ (el, ) for el in range(bitsLabel) ]
    swapMasks2 = [ c for c in combinations(range(bitsLabel), 2) ]

    return swapMasks1 + swapMasks2

def swapByMask(label, mask):
    """Swap bits in label according to a mask"""

    modLabel = [ c for c in label ]

    for bitNum in mask:
        if modLabel[bitNum] == '0':
            modLabel[bitNum] = '1'
        elif modLabel[bitNum] == '1':
            modLabel[bitNum] = '0'

    return "".join(modLabel)

def createLabelDict(nodeList):
    d = {}

    for i, node in enumerate(nodeList):
        if node not in d:
            d[node] = [i]
        else:
            d[node].append(i)

    return d

def implicitClustering(nodeList, maxDist=3, bitsLabel=24):
    
    numNodes = len(nodeList)
    ufstruct = uf.UnionFind(list(range(len(nodeList))))
    
    swapMasks = calculateMasks(bitsLabel)
    labelDict = createLabelDict(nodeList)

    numClusterings = 0
    for i, node1 in enumerate(nodeList):
        print("Node {} of {}".format(i, numNodes-1))
        for sameLabelIndex in labelDict[node1]:
            if sameLabelIndex != i:
                ufstruct.union(i, sameLabelIndex)

        for mask in swapMasks:
            modLabel = swapByMask(node1, mask)
            if modLabel in labelDict:
                for index in labelDict[modLabel]:
                    ufstruct.union(i, index)

    k = ufstruct.totalComponents #len(nodeList) - numClusterings
    return k


if __name__ == '__main__':
    print("Loading graph..")
    nodeList, labelBits = getGraph()
    print("Calculating clusters..")
    maxDist = 3
    k = implicitClustering(nodeList, maxDist, labelBits)
    print("Minimum number of clusters to ensure that members " + 
        "differ at most with 3 bits: {}".format(k))