class Solution:
    def isValid(self, s: str) -> bool:
        myMap = {
            '}' : '{',
            ']' : '[',
            ')' : '('
        }

        stack = []
        for c in s:
            if c == '[' or c == '{' or c == '(':
                stack.append(c)
            else:
                if len(stack):
                    if stack[-1] == myMap[c] :
                        stack.pop()
                    else:
                        return False
                else:
                    return False

        return len(stack) == 0