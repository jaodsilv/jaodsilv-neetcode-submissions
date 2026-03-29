'''
How to make all operation O(1)?
So far what I got is:
- O(1) for most operations
- O(n) for pop xor push xor getMin

If I use a heap, to keep track of the min, I get log(n) for the push AND pop, which improve things a bit

Perhaps a hash table?
Or maybe a linkedlist?
or a prefix list?
'''
class MinStack:

    def __init__(self):
        self.stack = []
        self.prefix = []
        self.min = None

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.prefix:
            self.prefix.append(min(val, self.prefix[-1]))
        else:
            self.prefix = [val]

    def pop(self) -> None:
        self.stack.pop()
        self.prefix.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.prefix[-1]
