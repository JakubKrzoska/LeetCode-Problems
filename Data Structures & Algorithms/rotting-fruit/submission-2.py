class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        time, fresh = 0, 0
        q = deque()
        visited = set()
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
                    visited.add((r, c))

        
        while q and fresh > 0:
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in direction:
                    row = x + dx
                    col = y + dy
                    if(row in range(0, ROWS) and col in range(0, COLS) and
                        grid[row][col] == 1 and (row, col) not in visited):
                        q.append((row, col))
                        visited.add((row, col))
                        fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1
            




                