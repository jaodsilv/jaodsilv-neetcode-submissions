from collections import deque
class Queue:
    def __init__(self) -> None:
        self.queue = deque()
    def push(self, value):
        self.queue.append(value)
    def peek(self):
        return self.queue[0]
    def pop(self):
        return self.queue.popleft()
    def size(self) -> int:
        return len(self.queue)
    def empty(self):
        return self.size() == 0

class MyStack:

    def __init__(self):
        self.queue = Queue()

    def push(self, x: int) -> None:
        queue = Queue()
        queue.push(x)
        queue.push(self.queue)
        self.queue = queue

    def pop(self) -> int:
        x = self.queue.pop()
        self.queue = self.queue.pop()
        return x

    def top(self) -> int:
        return self.queue.peek()

    def empty(self) -> bool:
        return self.queue.empty()        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()