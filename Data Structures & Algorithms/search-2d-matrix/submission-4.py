class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        bottom, top = 0, len(matrix) - 1

        while bottom <= top:
            mid_row = (bottom + top)//2
            if target > matrix[mid_row][-1]:
                bottom = mid_row + 1
            elif target < matrix[mid_row][0]:
                top = mid_row - 1
            else:
                break

        if not (bottom <= top):
            return False

        row = (bottom + top)//2
        l, r = 0, COLS - 1

        while l <= r:
            mid = (l+r)//2
            if target > matrix[row][mid]:
                l = mid + 1
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                return True
        return False


         




