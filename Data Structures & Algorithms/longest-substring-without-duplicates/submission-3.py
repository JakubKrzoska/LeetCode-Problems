class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = set()
        l = 0
        res = 1
        if not s:
            return 0
        for r in range(len(s)):
            if s[r] in letters:
                res = max(r - l, res)
                while s[r] in letters:
                    letters.remove(s[l])
                    l += 1
            letters.add(s[r])
        res = max(res, r-l+1)
        return res