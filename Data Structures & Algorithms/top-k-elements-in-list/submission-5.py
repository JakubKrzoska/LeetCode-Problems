class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        amounts = [[] for i in range(len(nums)+1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for key, value in count.items():
            amounts[value].append(key)
        
        res = []
        for i in range(len(amounts)-1, 0, -1):
            for n in amounts[i]:
                res.append(n)
                if len(res) == k:
                    return res

        