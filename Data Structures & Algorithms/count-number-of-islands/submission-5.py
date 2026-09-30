class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        h, l = len(grid), len(grid[0]) 

        def bfs(i, j, visted):
            q = collections.deque()
            q.append((i, j))
            visited.add((i, j))

            while q:
                x, y = q.popleft()
                directions = [(1, 0),(-1, 0),(0, 1),(0, -1)]
                for dx, dy in directions:
                    row = x + dx
                    col = y + dy
                    if (row in range(0, h) and col in range(0, l) and (row, col)
                        not in visited and grid[row][col] == "1"):
                            q.append((row, col))
                            visited.add((row, col)) 
        
        res = 0
        visited = set()
        for i in range(h):
            for j in range(l):
                if grid[i][j] == "1" and (i, j) not in visited:
                    bfs(i, j, visited)
                    res += 1
        return res




