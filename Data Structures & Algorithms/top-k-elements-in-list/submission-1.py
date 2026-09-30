class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        amounts = [[] for i in range(len(nums)+1)]

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        for key, value in freq.items():
            amounts[value].append(key)

        res = []
        for i in range(len(amounts)-1, 0, -1):
            for n in amounts[i]:
                res.append(n)
                if len(res) == k:
                    return res
