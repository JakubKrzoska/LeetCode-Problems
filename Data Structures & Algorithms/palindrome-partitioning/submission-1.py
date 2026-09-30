class Solution:
    def partition(self, s: str) -> List[List[str]]:    
        def isPalindrome(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        res = []
        stack = []

        def backtrack(i):
            if i >= len(s):
                res.append(stack.copy())
                return
            for j in range(i, len(s)):
                if isPalindrome(s, i, j):
                    stack.append(s[i:j+1])
                    backtrack(j + 1)
                    stack.pop()
        backtrack(0)
        return res
            

            
            
    