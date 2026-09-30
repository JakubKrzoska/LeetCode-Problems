class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])
        visited = set()
        visited.add((0,0))
        queue = deque()
        queue.append((0, 0))
        length = 0

        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

        while queue:
            for i in range(len(queue)):
                x, y = queue.popleft()
                if x == N-1 and y == M-1:
                    return length
                for dx, dy in directions:
                    row, col = x+dx, y+dy
                    if row == N or col == M or (row, col) in visited or min(row, col) < 0 or grid[row][col] == 1:
                        continue
                    visited.add((row, col))
                    queue.append((row, col))
            length += 1
        return -1

   
                


