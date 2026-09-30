class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = l + 1

        res = 0
        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            curr = prices[r] - prices[l]
            res = max(curr, res)
            r += 1

        return res 
