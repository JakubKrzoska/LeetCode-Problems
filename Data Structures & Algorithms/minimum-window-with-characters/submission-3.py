class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        wordCount, window = {}, {}
        for c in t:
            wordCount[c] = 1 + wordCount.get(c, 0)

        have, need = 0, len(wordCount)
        res, resLen = [-1, -1], float("inf")

        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            
            if c in wordCount and wordCount[c] == window[c]:
                have += 1
            
            while have == need:
                if (r - l) + 1 < resLen:
                    resLen = r - l + 1
                    res = [l, r]
                
                window[s[l]] -= 1
                if s[l] in wordCount and window[s[l]] < wordCount[s[l]]:
                    have -= 1
                l += 1
        
        return s[res[0]:res[1]+1] if res != float("inf") else ""





        
