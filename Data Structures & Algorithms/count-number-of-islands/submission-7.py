class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        res = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visited.add((r, c))

            while q:
                x, y = q.popleft()
                for dx, dy in directions:
                    row = x + dx
                    col = y + dy

                    if(row < 0 or row == ROWS or col < 0 or col == COLS or grid[row][col] != "1"
                        or (row, col) in visited):
                        continue
                    q.append((row, col))
                    visited.add((row, col))

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and grid[r][c] == "1":
                    bfs(r, c)
                    res += 1
        
        return res





