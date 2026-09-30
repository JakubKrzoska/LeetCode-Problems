class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N, M = len(profit), capacity
        cache = [[-1] * (M+1) for _ in range(N)]
        return self.dfs(0, capacity, profit, weight, cache)
    
    def dfs(self, i, capacity, profit, weight, cache):
        if i == len(profit):
            return 0
        if cache[i][capacity] != -1:
            return cache[i][capacity]

        #skip
        maxProfit = self.dfs(i+1, capacity, profit, weight, cache)

        #take
        newCap = capacity - weight[i]
        if newCap >= 0:
            maxTake = profit[i] + self.dfs(i, newCap, profit, weight, cache)
            maxProfit = max(maxProfit, maxTake)
        cache[i][capacity] = maxProfit
        return cache[i][capacity]
        