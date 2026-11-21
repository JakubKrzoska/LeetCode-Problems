class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0]*len(height)
        maxRight = [0]*len(height)
        minLeftRight = [0]*len(height)
        res = 0

        for i in range(1, len(height)):
            maxLeft[i] = max(maxLeft[i-1], height[i-1])
        
        for i in range(len(height) - 2, -1, -1):
            maxRight[i] = max(maxRight[i + 1], height[i+1])
        
        for i in range(len(height)):
            minLeftRight[i] = min(maxLeft[i], maxRight[i])
            res += max(0, minLeftRight[i] - height[i])
        
        return res
        

