class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N, M = len(profit), capacity
        cache = [[-1] * (M+1) for _ in range(N)]
        return self.dfs(0, capacity, profit, weight, cache)
    
    def dfs(self, i, capacity, profit, weight, visited):
        if i == len(profit):
            return 0
        if visited[i][capacity] != -1:
            return visited[i][capacity]

        #skip
        maxProfit = self.dfs(i+1, capacity, profit, weight, visited)

        #take
        newCap = capacity - weight[i]
        if newCap >= 0:
            p = profit[i] + self.dfs(i+1, newCap, profit, weight, visited)
            maxProfit = max(maxProfit, p)
        visited[i][capacity] = maxProfit

        return visited[i][capacity]    
        