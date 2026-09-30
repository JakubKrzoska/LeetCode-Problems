class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        for i in range(len(nums)):
            if i+1 < len(nums):
                prefix[i+1] = prefix[i] * nums[i]

        for i in range(len(nums)-1, -1, -1):
            if i-1 >= 0:
                postfix[i-1] = postfix[i] * nums[i]
        res = []
        for i in range(len(prefix)):
            res.append(prefix[i] * postfix[i])
        return res