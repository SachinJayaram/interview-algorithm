#!/usr/bin/env python

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs_traverse(self, s, visited):
        visited.add(s)
        print(s, end=' ')
        for i in self.graph[s]:
            if i not in visited:
                self.dfs_traverse(i, visited)

    def dfs(self, s):
        visited = set()
        self.dfs_traverse(s, visited)

if __name__ == '__main__':
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    
    print("Following is DFS from (starting from vertex 2)")
    g.dfs(2)