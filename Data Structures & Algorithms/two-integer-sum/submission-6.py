class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remindings = {}

        for i, n in enumerate(nums):
            rest = target - n
            if rest in remindings:
                return [remindings[rest], i]
            remindings[n] = i
        