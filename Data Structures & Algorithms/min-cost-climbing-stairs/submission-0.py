class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        res = [0]*(len(cost) +1)
        res[-2] = cost[-1] 
        for i in range(len(cost)-2, -1, -1):
            res[i] = cost[i] + min(res[i+1], res[i + 2])
        print(res)
        return min(res[0], res[1])