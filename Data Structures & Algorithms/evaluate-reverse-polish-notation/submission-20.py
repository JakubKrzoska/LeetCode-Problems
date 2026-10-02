class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for s in tokens:
            if s == "+":
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n1 + n2)
            elif s == '-':
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n2 - n1)
            elif s == '*':
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n1*n2)
            elif s == '/':
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(int(n2/n1))
            else:
                stack.append(int(s))
        
        return stack[0]
            

