class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        res = 0

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            curr = 1

            while q:
                for _ in range(len(q)):
                    x, y = q.popleft()
                    for dx, dy in directions:
                        row, col = x + dx, y + dy
                        if (row in range(0, ROWS) and col in range(0, COLS) and 
                            (row, col) not in visited and grid[row][col] == 1):
                            q.append((row, col))
                            visited.add((row, col))
                            curr += 1
            return curr

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    visited.add((r, c))
                    res = max(res, bfs(r, c))
        
        return res

        
