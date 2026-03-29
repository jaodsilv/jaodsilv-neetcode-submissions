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
        if self.min == popped:
            if self.stack:
                self.min = min(self.stack)
            else: 
                self.min = None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min


    '''
    ["MinStack" => null
    "push", 2147483646, [null
    "push", 2147483646,  ,null,
    "push", 2147483647, null,
    "top", 2147483647,
    "pop",null,
    "getMin",2147483646,
    "pop",null,
    "getMin", 2147483646,
    "pop", null,
    "push", 2147483647, null,
    "top",2147483647,
    "getMin", 2147483646 OR 2147483647,
    "push", -2147483648, null,
    "top", -2147483648,
    "getMin", -2147483648,
    "pop",null,
    "getMin",2147483647
    "pop"],null]
    '''
