class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            print(num ^ res)
            res = num ^ res
        return res