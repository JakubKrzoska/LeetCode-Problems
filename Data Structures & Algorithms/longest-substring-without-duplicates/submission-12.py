class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = set()
        if len(s) == 0:
            return 0

        l = 0
        r = l + 1
        letters.add(s[l])
        res = 1

        while r < len(s):
            while s[r] in letters:
                letters.remove(s[l])
                l += 1
            letters.add(s[r])
            r += 1
            res = max(res, r - l)
        
        return res
            