class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        queue = deque()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    queue.append((i, j))
                    visited.add((i, j))

        
        dist = 1
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (min(row, col) < 0 or row == ROWS or col == COLS or
                        (row, col) in visited or grid[row][col] == -1):
                        continue
                    grid[row][col] = dist
                    queue.append((row, col))
                    visited.add((row, col))
            dist += 1
