class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        amount = defaultdict(int)
        for c in s:
            amount[c] += 1
        for c in t:
            if amount[c] == 0:
                return False
            amount[c] -= 1
        for v in amount.values():
            if v != 0:
                return False
        return True
        