class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(r, c, res):
            q = deque()
            q.append((r, c))
            visited.add((r, c))
            temp = 1

            while q:
                for i in range(len(q)):
                    x, y = q.popleft()
                    for dx, dy in directions:
                        row = x + dx
                        col = y + dy
                        if(row in range(0, ROWS) and col in range(0, COLS) and
                            grid[row][col] == 1 and (row, col) not in visited):
                            q.append((row, col))
                            visited.add((row, col))
                            temp += 1
            res = max(res, temp)
            return res
                


        
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    res = bfs(r, c, res)
        return res
