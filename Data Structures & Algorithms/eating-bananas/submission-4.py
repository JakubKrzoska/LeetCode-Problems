class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == h:
            return max(piles)
        l, r = 1, max(piles)

        while l <= r:
            time = 0
            mid = (l + r)//2
            
            for banan in piles:
                time += math.ceil(banan/mid)
            
            if time > h:
                l = mid + 1
            else:
                r = mid - 1
        
        return l
