class MinStack:

    def __init__(self):
        self.stack = []
        self.monotonic = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.monotonic:
            self.monotonic.append(val)
        else:
            if self.monotonic[-1] >= val:
                self.monotonic.append(val)

    def pop(self) -> None:
        if self.stack:
            x = self.stack.pop()
        if self.monotonic[-1] == x :
            self.monotonic.pop()
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        return self.monotonic[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()