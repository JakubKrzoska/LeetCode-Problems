class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])

        res = 0
        for i in range(2, len(nums) - 1):
            print(i)
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        res = max(res, dp[len(nums)-2])

        dp = [0]*len(nums)
        dp[1] = nums[1]
        dp[2] = max(dp[1], nums[2])

        for i in range(3, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        res = max(res, dp[len(nums) - 1])

        return res
        
