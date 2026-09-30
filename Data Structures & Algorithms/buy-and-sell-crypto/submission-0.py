class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        res = 0
        for r in range(len(prices)):
            while l < r and prices[l] > prices[r]:
                l += 1
            tmp = (prices[r] - prices[l])
            res = max(tmp, res)
        return res  