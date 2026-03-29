'''
class Node:
    def __init__(self, val, count = 0, left = None):
        self.val = val
        self.count = count
        self.left = left
        self.right = None

    def _swapLeft(self) -> bool:
        if self.left is None or self.left.count > self.count:
            return False

        left = self.left
        leftleft = left.left
        right = self.right

        self.right = left
        self.left = leftleft
        left.left = self
        left.right = right
        return True

    def _swapRight(self) -> bool:
        if self.right is None or self.right.count < self.count:
            return False

        right = self.right
        rightright = right.right
        left = self.left

        self.left = right
        self.right = rightright
        right.right = self
        right.left = left
        return True

    def add(self):
        self.count += 1
        while self._swapLeft():
            pass

    def sub(self):
        self.count -= 1
        while self._swapRight():
            pass

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f'{self.val}: {self.count}'

class DoubledLinkedList:
    def __init__(self):
        self.nodes = [None]*26
        self.head = None
        self.tail = None

    def add(self, char):
        node = self.getNode(char)
        node.add()
        self._updateHeadTail()
    
    def sub(self, char):
        node = self.getNode(char)
        node.sub()
        self._updateHeadTail()
        # print(f'node count: {node.count}')
        # print(f'node left: {node.left}')
        # print(f'node right: {node.right}')
        if node.count == 0:
            self.nodes[self._index(char)] = None
            if node.left is None:
                # Means this is the only node
                self.head = None
                self.tail = None
            else:
                node.left.right = None
                self.tail = node.left


    def getNode(self, char):
        index = self._index(char)
        node = self.nodes[index]
        if node is None:
            node = Node(char)
            self.nodes[index] = node
            if self.head is None:
                self.head = node
                self.tail = node
            else:
                self.tail.right = node
                node.left = self.tail
                self.tail = node

        return node

    def _updateHeadTail(self):
        if self.head.left:
            self.head = self.head.left
        if self.tail.right:
            self.tail = self.tail.right


    def _index(self, char):
        return ord(char) - ord('A')

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        node = self.head
        s = '['
        while node and node.right:
            s = s + str(node) + ', '
            node = node.right
        if node:
            s = s + str(node)
        return s + ']'

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
                
        ll = DoubledLinkedList()
        
        maxLength = 0
        i = 0
        j = 0
        count = 0
        while i < len(s):
            count += 1
            if count == 20:
                return maxLength
            ll.add(s[i])
            print(ll)
            i += 1
            while i < len(s) and ll.head.count + k > i - j:
                # print('ll.head.count + k > i - j + 1 =>', ll.head.count, '+', k, '>', i, '-', j, '=>', ll.head.count + k, '>', i - j)
                ll.add(s[i])
                # print(ll)
                i += 1
            while j < i and ll.head.count + k < i - j:
                # print('ll.head.count + k < i - j =>', ll.head.count, '+', k, '<', i, '-', j, '=>', ll.head.count + k, '<', i - j)
                # print(f's[j] = s[{j}] = {s[j]}')
                ll.sub(s[j])
                # print(ll)
                j += 1
            maxLength = max(maxLength, i - j)
        return maxLength
'''

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
