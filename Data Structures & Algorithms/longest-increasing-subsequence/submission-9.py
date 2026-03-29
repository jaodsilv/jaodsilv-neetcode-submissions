import heapq
from collections import deque
import bisect
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
        1 [5+1,4+1,3+1,2+1,1+1,0+1,0]
        0 [  1,  1,  1,  1,  1,  1,1] # always with 0 size

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

        maxVal = max(nums)
        minVal = max(nums)
        values = sorted(set(nums))

        minHeap = [(n, i) for i, n in enumerate(nums)]
        heapq.heapify(minHeap)
        queue = deque()
        while minHeap:#O(nlogn + n²) = O(n²)
            print(queue)
            val, index = heapq.heappop(minHeap) #O(logn)
            print(val, index)
            added = False
            lastLen=len(nums)
            for i in range(1, len(queue)+1): #O(n², amortized to O(3n)=O(n))
                res = queue[-i]
                if added and len(res) < lastLen:
                    break
                if res[-1][0] < val and res[-1][1] < index:
                    lastLen = len(res)
                    clone = res.copy() #O(n)
                    clone.append((val,index))
                    index = bisect.bisect_left(queue, len(clone), lo=max(0,len(queue)-i-1), key=lambda x: len(x)) #O(logn)
                    queue.insert(index, clone) #O(n)
                    added = True
            if not added:
                queue.appendleft([(val, index)])
        return len(queue[-1])

