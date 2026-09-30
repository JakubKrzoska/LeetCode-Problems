class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bott = 0, ROWS - 1
        
        while top <= bott:
            mid = (top + bott) // 2
            if target > matrix[mid][-1]:
                top += 1
            elif target < matrix[mid][0]:
                bott -= 1
            else:
                break
            
        if not (top <= bott):
            return False

        l, r = 0, COLS - 1
        row = (top + bott) // 2
        while l <= r:
            mid = (l+r) // 2
            if target < matrix[row][mid]:
                r -= 1
            elif target > matrix[row][mid]:
                l += 1
            else:
                return True
        return False



