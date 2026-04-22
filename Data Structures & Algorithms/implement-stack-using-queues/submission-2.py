from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def push(self, x):
        self.queue.append(x)

    def pop(self):
        if self.queue:
            return self.queue.popleft()
        return 0
    def peek(self):
        if self.queue[0]:
            return self.queue[0]
        return 0

    def __len__(self) -> int:
        return len(self.queue)

class MyStack:

    def __init__(self):
        self.q = Queue()
        self.q.push(None)
        # self.queue2 = Queue()
        # self.topElement = 0

    def push(self, x: int) -> None:
        newQ = Queue()
        newQ.push(x)
        newQ.push(self.q)
        self.q = newQ

    def pop(self) -> int:
        x = self.q.pop()
        self.q = self.q.pop()
        return x

    def top(self) -> int:
        return self.q.peek()

    def empty(self) -> bool:
        return len(self.q) == 1

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()