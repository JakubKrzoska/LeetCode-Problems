class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        N = len(temperatures)
        res = [0]*N
        stack = []

        for i, v in enumerate(temperatures):
            while stack and stack[-1][1] < v:
                inx, temp = stack.pop()
                res[inx] = i - inx
            stack.append((i, v))
        
        return res

            