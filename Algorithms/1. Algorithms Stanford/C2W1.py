#Implement SCC with kosaraju Algorithm

import csv
import sys
import threading
threading.stack_size(67108864)
sys.setrecursionlimit(2**20)

from collections import defaultdict

def reverse(graph):
    new_graph = defaultdict(list)
    for u in graph:
        for v in graph[u]:
            new_graph[v].append(u)
    return new_graph

def first_pass(graph):
    seen = set()
    ordering = []

    def dfs(v):
        seen.add(v)
        for u in graph[v]:
            if u not in seen:
                dfs(u)
        ordering.append(v)

    for u in graph.keys():
        if u not in seen:
            dfs(u)
    return ordering

def second_pass(graph, ordering):
    seen = set()
    leader = defaultdict(list)
    for u in reversed(ordering):
        if u not in seen:
            # Non recursive DFS using a stack
            seen.add(u)
            stack = [u]
            while stack:
                item = stack.pop()
                for v in graph[item]:
                    if v not in seen:
                        seen.add(v)
                        stack.append(v)
                leader[u].append(item)
    return leader

def kosaraju(graph):
    return second_pass(graph, first_pass(reverse(graph)))

def main():
    f = open('SCC.txt')
    graph = defaultdict(list)
    for line in f:
        u, v = line.strip().split()
        graph[u].append(v)
    sccs = kosaraju(graph).values()
    print sorted(map(len, sccs))[::-1][:10]



if __name__ == '__main__':
    thread = threading.Thread(target=main)
    thread.start()