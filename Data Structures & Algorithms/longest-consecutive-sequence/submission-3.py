class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)

        res = 0
        for num in nums:
            if (num-1) not in numbers:
                length = 1
                while(num + length) in numbers:
                    length += 1
                res = max(res, length)
        return res
            