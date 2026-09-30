class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.isValid(s[l]):
                l += 1

            while l < r and not self.isValid(s[r]):
                r -= 1

            if s[l].upper() != s[r].upper():
                return False
            l += 1
            r -= 1
        return True
                
            


    def isValid(self, s):
        return(ord('a') <= ord(s) <= ord('z') or
                ord('A') <= ord(s) <= ord('Z') or 
                ord('0') <= ord(s) <= ord('9'))
    
        