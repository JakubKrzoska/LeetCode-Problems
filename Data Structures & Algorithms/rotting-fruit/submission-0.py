class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        queue = deque()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    queue.append((i, j))
                    visited.add((i, j))

        time = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (min(row, col) < 0 or row == ROWS or col == COLS or
                        (row, col) in visited or grid[row][col] == 0):
                        continue
                    visited.add((row, col))
                    queue.append((row, col))
                    grid[row][col] = 2
            if len(queue) > 0:
                time += 1
            
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    return -1
        return time
                