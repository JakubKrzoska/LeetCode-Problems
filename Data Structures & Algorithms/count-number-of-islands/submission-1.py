class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set()
        res = 0

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            visited.add((r, c))
            
            while queue:
                row, col = queue.popleft()
                directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if r in range( ROWS) and c in range (COLS) and grid[r][c] == '1' and (r, c) not in visited:
                        queue.append((r, c))
                        visited.add((r, c))
                    

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and grid[r][c] == '1':
                    bfs(r, c)
                    res += 1

                    
        return(res)