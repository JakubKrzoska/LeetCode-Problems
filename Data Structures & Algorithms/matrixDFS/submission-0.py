class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        visited = set()
        N = len(grid)
        M = len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(x, y, visited):
            if (x, y) in visited or min(x, y) < 0 or x == N or y == M or grid[x][y] == 1:
                return 0
            if x == N-1 and y == M-1:
                return 1
            visited.add((x, y))

            count = 0
            count += dfs(x+1, y, visited)
            count += dfs(x-1, y, visited)
            count += dfs(x, y+1, visited)
            count += dfs(x, y-1, visited)
            visited.remove((x, y))
            return count

        res = dfs(0, 0, visited)

        return res