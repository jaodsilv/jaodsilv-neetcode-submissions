from collections import defaultdict
class FreqStack:
    '''
    [5, 7, 5, 7, 4, 5]
    '''

    def __init__(self):
        self.vals = [[]]
        self.freqs = defaultdict(int)

    def push(self, val: int) -> None:
        self.freqs[val] += 1
        if self.freqs[val] == len(self.vals):
            self.vals.append([val])
        else:
            self.vals[self.freqs[val]].append(val)

    def pop(self) -> int:
        if not self.vals[-1]:
            self.vals.pop()
        res = self.vals[-1].pop()
        self.freqs[res] -= 1
        return res

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()