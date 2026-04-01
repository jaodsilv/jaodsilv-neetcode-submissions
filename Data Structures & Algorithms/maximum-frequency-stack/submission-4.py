from collections import defaultdict
class FreqStack:

    def __init__(self):
        self.cnt = defaultdict(int)
        self.stacks = [[]]

    def push(self, val: int) -> None:
        self.cnt[val] += 1
        if self.cnt[val] == len(self.stacks):
            self.stacks.append([val])
        else:
            self.stacks[self.cnt[val]].append(val)

    def pop(self) -> int:
        last = self.stacks[-1]
        res = last.pop()
        self.cnt[res] -= 1
        if len(self.stacks[-1]) == 0:
            self.stacks.pop()
        return res
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()