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
        self.stack = Stack()
        self.last = None

    def push(self, x: int) -> None:
        '''
        pushing order: [1, 2, 3]
        Making it in O(1) and in a way the pop is also O(1)
        [1]
        [[2], 1]
        [[[3], 2], 1]
        So we need to keep the pointer to the last stack
        '''
        if self.stack.empty():
            self.stack.push(x)
            self.last = self.stack
        else:
            last = self.last

            self.last = Stack()
            self.last.push(x)

            prev = last.pop()
            last.push(self.last)
            last.push(prev)
        
    def pop(self) -> int:
        '''
        popping order: [1, 2, 3]
        [[[3], 2], 1]
        [[3], 2]
        [3]
        So we need to keep the pointer to the last stack
        '''
        first = self.stack.pop()
        if not self.stack.empty():
            self.stack = self.stack.pop()

        return first

    def peek(self) -> int:
        return self.stack.peek()
        
    def empty(self) -> bool:
        return self.stack.empty()
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()