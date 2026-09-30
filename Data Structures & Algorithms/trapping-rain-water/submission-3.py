class Solution:
    def trap(self, heights: List[int]) -> int:
        if not heights: return 0
        
        res = 0
        l, r = 0, len(heights) - 1
        maxLeft, maxRight = heights[l], heights[r]

        while l < r:
            if maxLeft < maxRight:
                l += 1
                maxLeft = max(maxLeft, heights[l])
                res += maxLeft - heights[l]
            else:
                r -= 1
                maxRight = max(maxRight, heights[r])
                res += maxRight - heights[r]

        return res
