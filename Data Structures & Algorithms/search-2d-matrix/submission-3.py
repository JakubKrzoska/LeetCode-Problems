class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        bot, top = 0, ROWS - 1

        while bot <= top:
            mid_row = (bot + top)//2
            if target > matrix[mid_row][-1]:
                bot = mid_row + 1
            elif target < matrix[mid_row][0]:
                top = mid_row - 1
            else:
                break
            
        if not (bot <= top):
            return False

        row = (top + bot)//2
        l, r = 0, COLS - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] > target:
                r = mid - 1
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                return True
        
        return False
         




