class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paren = {
            '}' : '{',
            ']' : '[',
            ')' : '('
        }

        for c in s:
            if c not in paren:
                stack.append(c)
            elif c in paren:
                if stack and paren[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return True if not stack else False