class Node:
    def __init__(self, left):
        # self.val = val
        self.count = 0
        self.left = left
        self.right = None
        if left is not None:
            left.right = self

    def add(self):
        self.count += 1
        self._swiftUp()

    def sub(self):
        self.count -= 1
        return self._swiftDown()

    def _swiftDown(self):
        isHead = self.left is None
        head = None
        while self.right and self.right.count > self.count:
            r = self.right
            l = self.left
            rr = self.right.right
            r.left = l
            r.right = self
            self.right = rr
            self.left = r

            if l:
                l.right = r
            if rr:
                rr.left = self
            if isHead:
                isHead = False
                head = self.left
        return head

    def _swiftUp(self):
        while self.left and self.left.count <= self.count:
            l = self.left
            r = self.right
            ll = self.left.left
            l.right = r
            l.left = self
            self.left = ll
            self.right = l

            if r:
                r.left = l
            if ll:
                ll.right = self

class LL:
    def __init__(self, k, s=""):
        self.k = k
        self.nodes = [None]*26
        self.tail = None
        self.head = None
        self.len = 0
        for c in s:
            if self.isValid():
                self.add(c)
            else:
                return

    def _ctoi(self, c):
        return ord(c) - ord('A')

    def _itoc(self, i):
        return chr(i + ord('A'))

    def isValid(self):
        if self.head:
            return self.head.count + self.k >= self.len
        else:
            return self.k >= self.len

    def add(self, c) -> bool:
        node = self.nodes[self._ctoi(c)]
        if node is None:
            node = Node(self.tail)
            self.nodes[self._ctoi(c)] = node
            self.tail = node
        node.add()
        self.len += 1
        if self.head is None:
            self.tail = node
            self.head = node
            return True
        if node.left is None:
            self.head = node
        return node.left is None

    def sub(self, c) -> bool:
        node = self.nodes[self._ctoi(c)]
        maybeHead = node.sub()
        if node.count == 0:
            self.nodes[self._ctoi(c)] = None
            if node.left is None:
                self.head = None
                self.tail = None
            else:
                node.left.right = None
        self.len -= 1
        if maybeHead is not None:
            self.head = maybeHead

    def printNodes(self):
        if self.nodes[0] is None:
            print("[None", end='')
        else:
            print(f'[A: {self.nodes[0].count}', end='')
        for i in range(1, 26):
            if self.nodes[i] is None:
                print(", None", end='')
            else:
                print(f", {self._itoc(i)}: {self.nodes[i].count}", end = '')
        print(']')

    def printLL(self):
        if self.head is None:
            print('[]')
        # print(f'Head: {self.head.count}')
        # print(f'Tail: {self.tail.count}')
        node = self.head
        print('[', end = '')
        while node:
            if node.right:
                print(node.count, end=', ')
            else:
                print(f'{node.count}]')
            node = node.right

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ll = LL(k, s)
        if ll.isValid():
            return len(s)
        res = ll.len - 1
        ll.printLL()
        ll.printNodes()

        for i in range(ll.len, len(s)):
            while ll.len > 1 and not ll.isValid():
                ll.sub(s[i - ll.len])
                print(f'Valid: {ll.isValid()}. sub: index: {i - ll.len + 1}, val: {s[i - ll.len + 1]}')
                ll.printNodes()
            c = s[i]
            ll.add(c)
            ll.printLL()
            ll.printNodes()
            if ll.isValid():
                res = max(res, ll.len)
            else:
                res = max(res, ll.len - 1)
            print(res)
            ll.printLL()
            ll.printNodes()
        return res
            
