class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        minH = [(grid[0][0], 0, 0)]
        visited = set()
        visited.add((0, 0))
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while minH:
            h, r, c = heapq.heappop(minH)
            visited.add((r, c))

            if r == N - 1 and c == N - 1:
                return h
            
            for dr, dc in directions:
                new_x = r + dr
                new_y = c + dc
                if (min(new_x, new_y) < 0 or max(new_x,new_y) >= N or 
                    (new_x, new_y) in visited):
                    continue
                heapq.heappush(minH, (max(h, grid[new_x][new_y]), new_x, new_y))
        

            
