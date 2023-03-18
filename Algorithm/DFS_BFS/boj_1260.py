# https://www.acmicpc.net/problem/1260
from collections import deque
import sys
from typing import MutableSequence,Any

def DFS(graph:dict,starting_node:Any):
    def aDFS(node:Any):
        visited_stack.append(node)
        for i in graph[node]:
            if i not in visited_stack:
                aDFS(i)
    visited_stack = list()
    aDFS(starting_node)
    print(" ".join(map(str,visited_stack)))

def BFS(graph:dict,starting_node:Any):
    visited_queue = deque([])
    result = list()
    result.append(starting_node)
    visited_queue.extend(graph[starting_node])
    while visited_queue:
        n = visited_queue.popleft()
        if n not in result:
            result.append(n)
            visited_queue.extend(graph[n])
    print(" ".join(map(str,result)))
    
if __name__ == "__main__":
    graph = dict()
    vertex,edge,starting_node = list(map(int,sys.stdin.readline().split()))
    for i in range(1,vertex + 1):
        graph[i] = list()
    for _ in range(edge):
        i,j = list(map(int,sys.stdin.readline().split()))
        graph[i].append(j)
        graph[j].append(i)
    for i,j in graph.items():
        graph[i] = sorted(j)
    DFS(graph,starting_node)
    BFS(graph,starting_node)