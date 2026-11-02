class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minimum = min(self.minimum, val)
        return

    def pop(self) -> None:
        self.stack.pop()
        self.minimum = min(self.stack)
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minimum
