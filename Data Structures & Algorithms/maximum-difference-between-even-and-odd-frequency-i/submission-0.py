class Solution:
    def maxDifference(self, s: str) -> int:
        counts = {}

        for c in s:
            counts[c] = 1 + counts.get(c, 0)

        currMax = -100000
        currMin = 1000000

        for val in counts.values():
            if val % 2:
                if val > currMax:
                    currMax = val
            elif val % 2 == 0:
                if val < currMin:
                    currMin = val
        
        return currMax - currMin 
                
        
       