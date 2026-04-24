class Stack:
    def __init__(self, elements = None) -> None:
        if elements:
            self.stack = elements
        else:
            self.stack = []
    def push(self, item) -> None:
        self.stack.append(item)
    def peek(self):
        return self.stack[-1]
    def pop(self):
        return self.stack.pop()
    def empty(self):
        return len(self.stack) == 0

class MyQueue:

    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def push(self, x: int) -> None:
        if not self.stack2.empty():
            while not self.stack2.empty():
                self.stack1.push(self.stack2.pop())
        self.stack1.push(x)
        
    def pop(self) -> int:
        if self.stack2.empty():
            while not self.stack1.empty():
                self.stack2.push(self.stack1.pop())

        return self.stack2.pop()

    def peek(self) -> int:
        if self.stack2.empty():
            while not self.stack1.empty():
                self.stack2.push(self.stack1.pop())

        return self.stack2.peek()
        
    def empty(self) -> bool:
        return self.stack1.empty() and self.stack2.empty()
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()