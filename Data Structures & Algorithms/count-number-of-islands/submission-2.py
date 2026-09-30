class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        res = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(r, c):
            nonlocal res
            visited.add((r, c))
            queue = deque()
            queue.append((r, c))
            res += 1

            while queue:
                for i in range(len(queue)):
                    r, c = queue.popleft()
                    for dr, dc in directions:
                        row, col = r + dr, c + dc
                        if (min(row, col) < 0 or row == ROWS or col == COLS or
                        (row, col) in visited or grid[row][col] == "0"):
                            continue
                        visited.add((row, col))
                        queue.append((row, col))

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1" and (i, j) not in visited:
                    bfs(i, j)
        return res
                        




