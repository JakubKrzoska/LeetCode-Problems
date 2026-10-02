class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        l, r = 0, ROWS - 1
        correctRow = ROWS

        while l <= r:
            mid = (l + r)//2

            if target >= matrix[mid][0] and target <= matrix[mid][COLS-1]:
                correctRow = mid
                break
            elif target > matrix[mid][COLS-1]:
                l = mid + 1
            elif target < matrix[mid][0]:
                r = mid - 1
                
        if correctRow == ROWS:
            return False
        
        l, r = 0, COLS - 1

        while l <= r:
            mid = (l + r)//2

            if matrix[correctRow][mid] == target:
                return True
            elif matrix[correctRow][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False

