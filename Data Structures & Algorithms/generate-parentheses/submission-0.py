class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack, res = [], []

        def dfs(start, end):
            if start == end == n:
                res.append("".join(stack))
                return
            
            if start < n:
                stack.append('(')
                dfs(start+1, end)
                stack.pop()
            
            if end < start:
                stack.append(')')
                dfs(start, end+1)
                stack.pop()
        
        dfs(0, 0)
        return res