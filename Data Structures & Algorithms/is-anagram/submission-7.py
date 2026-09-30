from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dist1 = {}
        dist2 = {}

        for c in s:
            if c in dist1:
                dist1[c] = dist1[c] + 1
            else:
                dist1[c] = 0
            
        for c in t:
            if c in dist2:
                dist2[c] = dist2[c] + 1
            else:
                dist2[c] = 0
        return dist1 == dist2
        
        