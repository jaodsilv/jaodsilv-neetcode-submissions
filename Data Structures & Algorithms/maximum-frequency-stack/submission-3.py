from collections import defaultdict
class FreqStack:

    def __init__(self):
        self.cnt = defaultdict(int)
        self.stacks = defaultdict(list)
        self.maxCnt = 0

    def push(self, val: int) -> None:
        self.cnt[val] += 1
        self.stacks[self.cnt[val]].append(val)
        self.maxCnt = max(self.maxCnt, self.cnt[val])
    def pop(self) -> int:
        res = self.stacks[self.maxCnt].pop()
        self.cnt[res] -= 1
        if len(self.stacks[self.maxCnt]) == 0:
            self.maxCnt -= 1
        return res
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()