class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        amount = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in amount:
                return [amount[diff], i]
            amount[n] = i 
        
        
        

