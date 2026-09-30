class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_set = set()
        for i in nums:
            if i in new_set:
                return True
            else:
                new_set.add(i)
        return False