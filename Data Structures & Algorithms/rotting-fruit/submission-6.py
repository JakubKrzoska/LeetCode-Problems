class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        bad_bananas = deque()
        visited = set()
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        good_bananas = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    bad_bananas.append((i, j))
                    visited.add((i, j))
                elif grid[i][j] == 1:
                    good_bananas += 1

        while bad_bananas and good_bananas > 0:
            for i in range(len(bad_bananas)):
                x, y = bad_bananas.popleft()

                for dx, dy in directions:
                    row, col = dx + x, dy + y
                    if (row < 0 or row == ROWS or col < 0 or col == COLS or
                        grid[row][col] != 1 or (row, col) in visited):
                        continue
                    else:
                        visited.add((row, col))
                        bad_bananas.append((row, col))
                        good_bananas -= 1
            res += 1
        

        return res if good_bananas == 0 else -1

