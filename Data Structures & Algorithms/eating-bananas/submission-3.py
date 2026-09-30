class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        res = r
        while l <= r:
            mid = (l + r)//2
            curr = 0
            for p in piles:
                curr += math.ceil(p/mid)
            if curr <= h:
                res = min(res, mid)
                r = mid - 1
            elif curr > h:            
                l = mid + 1
            
        return res


