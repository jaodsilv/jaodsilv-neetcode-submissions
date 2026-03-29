class MinStack:

    def __init__(self):
        self.stack = []
        self.min = None


    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min is None or val < self.min:
            self.min = val

    def pop(self) -> None:
        popped = self.stack.pop()
        if self.stack:
            if popped == self.min:
                self.min = min(self.stack)
        else:
            self.min = None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min
