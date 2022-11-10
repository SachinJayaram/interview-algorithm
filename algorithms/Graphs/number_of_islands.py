#!/usr/bin/env python


from collections import defaultdict, deque


class Graph:

    def dfs(self, i, j, grid):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
            return None
        grid[i][j] = '#'
        self.dfs(i, j+1, grid)
        self.dfs(i, j-1, grid)
        self.dfs(i+1, j, grid)
        self.dfs(i-1, j, grid)

    def num_islands(self, grid):
        """!
        Get the number of islands.
        Time complexity O(MXN)
        Space Complexity O(MXN).
        """
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(i, j, grid)
                    islands += 1

        return islands

    def num_islands_bfs(self, grid):
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    islands += 1
                    stack = [[i, j]]
                    while stack:
                        p, q = stack.pop()
                        if p > 0 and grid[p-1][q] == '1':
                            stack.append([p-1, q])
                        if p < len(grid) - 1 and grid[p+1][q] == '1':
                            stack.append([p+1, q])
                        p, q = stack.pop()
                        if q > 0 and grid[p][q-1] == '1':
                            stack.append([p, q-1])
                        if q < len(grid[0]) - 1 and grid[p][q+1] == '1':
                            stack.append([p, q+1])
                        grid[p][q] = '#'
        
        return islands



if __name__ == '__main__':
    grid = [["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]]
    grid_obj = Graph()
    print(grid_obj.num_islands(grid))
    print(grid_obj.num_islands_bfs(grid))