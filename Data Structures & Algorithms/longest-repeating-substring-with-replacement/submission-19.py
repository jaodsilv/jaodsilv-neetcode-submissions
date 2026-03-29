class Count:
    def __init__(self, val, count = 0):
        self.val = val
        self.count = count
        self.index = -1

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f'{self.val}: ({self.count}, {self.index})'

class Counter:
    def __init__(self):
        self.counts = [None]*26
        self.sorted = []

    def add(self, char):
        count = self.getCount(char)
        count.count += 1
        index = count.index
        # We could replace this by a heap
        while index > 0 and count.count > self.sorted[index-1].count:
            self.sorted[index - 1].index = index
            self.sorted[index], self.sorted[index - 1] = self.sorted[index - 1], self.sorted[index]
            index -= 1
        #print(self.sorted)
        count.index = index
    
    def sub(self, char):
        count = self.getCount(char)
        count.count -= 1
        index = count.index
        while index < len(self.sorted) - 1 and count.count < self.sorted[index+1].count:
            self.sorted[index + 1].index = index
            self.sorted[index], self.sorted[index + 1] = self.sorted[index + 1], self.sorted[index]
            index += 1
        count.index = index

        if count.count == 0:
            self.counts[self._index(char)] = None
            self.sorted.pop()

    def getCount(self, char):
        index = self._index(char)
        count = self.counts[index]
        if count is None:
            count = Count(char)
            self.counts[index] = count
            count.index = len(self.sorted)
            self.sorted.append(count)
        #print('GetCount', count, count.index)

        return count

    def _index(self, char):
        return ord(char) - ord('A')

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        if len(self.sorted) == 0:
            return '[]'

        s = '['
        for count in self.counts[:-1]:
            s = s + str(count) + ', '
        return s + str(self.counts[-1]) + ']'

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if k == 0:
            cur = 0
            curChar = s[0]
            maxi = 1
            for c in s:
                if c == curChar:
                    cur += 1
                else:
                    curChar = c
                    maxi = max(maxi, cur)
                    cur = 1
            return max(maxi, cur)
                
        counter = Counter()
        
        maxLength = 0
        i = 0
        j = 0
        #count = 0
        while i < len(s):
            #count += 1
            #if count == 20:
            #    return maxLength
            counter.add(s[i])
            #print(counter)
            i += 1
            while i < len(s) and counter.sorted[0].count + k > i - j:
                # print('counter.head.count + k > i - j + 1 =>', counter.head.count, '+', k, '>', i, '-', j, '=>', counter.head.count + k, '>', i - j)
                counter.add(s[i])
                # print(counter)
                i += 1
            while j < i and counter.sorted[0].count + k < i - j:
                # print('counter.head.count + k < i - j =>', counter.head.count, '+', k, '<', i, '-', j, '=>', counter.head.count + k, '<', i - j)
                # print(f's[j] = s[{j}] = {s[j]}')
                counter.sub(s[j])
                # print(counter)
                j += 1
            maxLength = max(maxLength, i - j)
        return maxLength
