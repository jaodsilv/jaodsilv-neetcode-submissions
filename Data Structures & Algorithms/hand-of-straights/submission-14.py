from collections import deque
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n == 0:
            return True
        if n % groupSize != 0:
            return False
        
        hand.sort()
        print(hand)
        queue = deque() # Each element a pair of number of values in the group
        curr = hand[0]
        prev = curr
        i = 0
        while i < len(hand):
            print(0, i, queue)
            if (not queue or curr == prev):
                queue.append(1)
                i += 1
                if i < n:
                    prev = curr
                    curr = hand[i]
            else:
                for j in range(len(queue)):
                    if curr != prev + 1:
                        return False
                    queue[j] += 1
                    i += 1
                    if i < len(hand):
                        curr = hand[i]
                prev = hand[i-1]
            while queue and queue[0] == groupSize:
                queue.popleft()
            
            print(1, i, queue)
        return len(queue) == 0
