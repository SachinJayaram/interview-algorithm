#!/usr/bin/env python


from collections import defaultdict, deque

class Graph:
    def __init__(self) -> None:
        self.graph = defaultdict(list)

    def add_edge(self, u, v) -> None:
        self.graph[u].append(v)

    def bfs(self, s):
        queue = deque([s])
        visited = [False] * (max(self.graph)+1)
        visited[s] = True
        while queue:
            s = queue.popleft()
            print(s, end='')
            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True


if __name__ == '__main__':
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    print("Following is Breadth First Traversal"
                  " (starting from vertex 2)")
    print("0->1, 0->2, 1->2, 2->0, 2->3, 3->3")
    g.bfs(2)


