import heapq
from collections import deque
import bisect

class Node:
    def __init__(self, val: int, L:int , R: int, left=None, right=None):
        self.val = val
        self.L = L
        self.M = (L+R)//2
        self.R = R
        self.left = left
        self.right = right

class SegmentTree:
    def __init__(self, n: int):
        self.N = n
        self.root = self.createNode(0, n-1)
        
    def createNode(self, L: int, R: int) -> Node:
        if L == R:
            return Node(0, L, L)
        m = (L+R)//2
        left = self.createNode(L, m)
        right = self.createNode(m+1, R)
        return Node(0, L, R, left, right)

    def update(self, index: int, val: int):
        node = self.root

        stack = [node]
        while node and node.L != node.R:
            if index <= node.M:
                node = node.left
            else:
                node = node.right
            stack.append(node)

        while stack:
            node = stack.pop()
            if node.L == node.R:
                node.val = val
            else:
                node.val = max(node.left.val, node.right.val)

    def query(self, L:int, R:int, node=None):
        if L > R:
            return 0
        if node is None:
            return self.query(L, R, self.root)
        if node.L == L and node.R == R:
            return node.val
        if R <= node.M:
            return self.query(L, R, node.left)
        if L > node.M:
            return self.query(L, R, node.right)
        return max(self.query(L,node.M,node.left), self.query(node.M+1, R, node.right))


        
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
            We can go building sequences bsed on the minimum diff and maximum length
            Let's say we have the sequence [a,b,c,d,e,f,g]
            We start building with [a]
            if b <= a:
                we add a new subsequence to our pool [b],
                since [b] and [a] have the same length we can drop [a]
            We can use a heap to keep track of the sequence lengths
            if b>a:
                we add a new subsequence to our pool [a,b]
            Let's continue with [a,b] and [a]
            if c < a:
                drop [a]
                add [c]
                keep [a,b]
            if c==a:
                ignore c
            if a < c < b:
                drop [a,b]
                keep [a]
                add [a,c]
            if c >= b:
                add [a,b,c]


            s [  0,  3,  1,  3,  2,  3,-]
            6 [ *0, *0,  0,  0,  0,  0,0]
            5 [  0, *0, *0,  0,  0,  0,0]
            4 [  1,  0, *0, *0,  0,  0,0]
            3 [1+4,0+1,1+0,  0, *0,  0,0]
            2 [5+4,0+4,1+3,0+1,0+1,  0,0]
            1 [  6,  5,  4,  3,  2,  1,0]

            [   0,    3,    1,   0, 3,  2,  3, 5, 6, 4]
            [   6,    1,    4,   3, 1,  2,  1] max is 6, there is no way to get more than 6
            pop => (0, 3)
            pop => ()

            {0: [0,3], 1: [3], 2: [5], 3: [1,4,6], 4:[9], 5:[7],6:[8]}
            [(0,0)]
            [(0,0),(1,3)]
            [(0,0),(3,1)]
            [(0,0),(1,3),(2,5)]
            [(0,0),(1,3),(3,4)]
            [(0,0),(1,3),(2,5),(3,6)]
            [(0,0),(1,3),(2,5),(3,6),(4,9)]
            [(0,0),(1,3),(2,5),(3,6),(5,7)]
            [(0,0),(1,3),(2,5),(3,6),(4,9),(6,8)]
            [(0,0),(1,3),(2,5),(3,6),(5,7),(6,8)]
            We add only to the first sequence we find 
        '''

        values = sorted(set(nums))
        compressMap = {v: i for i, v in enumerate(values)}
        compress = [compressMap[v] for v in nums]
        tree = SegmentTree(len(nums))
        res = 0
        for num in compress:
            cur = tree.query(0, num - 1) + 1
            tree.update(num, cur)
            res = max(res, cur)

        return res
