class MinStack:

    def __init__(self):
        self.stack = []
        self.curMin = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.curMin[-1] if self.curMin else float("inf"))
        self.curMin.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.curMin.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.curMin[-1]
