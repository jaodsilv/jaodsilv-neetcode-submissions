import heapq
from collections import deque, defaultdict

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # First criteria is to be multiple of groupSize
        if groupSize == 1:
            return True

        if len(hand) % groupSize != 0:
            return False

        def solutionHeap():
            heapq.heapify(hand)
            groups = deque()
            while hand:
                next = hand[0] # 1, 2, 2
                if len(groups) == 0:
                    heapq.heappop(hand)
                    groups.append(1)
                    prev = next # 1
                    continue
                # Add all repeated not processed yet as new groups
                while hand and next == prev:
                    groups.append(1)
                    heapq.heappop(hand) # 3
                    if len(hand) == 0:
                        return False
                    next = hand[0]
                    # 1, 2, 2
                # We need building times of the next value
                for i in range(len(groups)):
                    if len(hand) == 0:
                        return False
                    next = heapq.heappop(hand) # 2
                    if next > prev + 1:
                        return False
                    groups[i] += 1
                while groups and groups[0] == groupSize:
                    groups.popleft()
                prev = next # prev = 2
            return len(groups) == 0

        def solutionFreqMap():
            # Build a freq map
            freqs = defaultdict(int)
            for n in hand:
                freqs[n] += 1
            
            init = min(hand)
            end = max(hand) + 1
            for i in range(init, end):
                if freqs[i] == 0:
                    continue
                count = freqs[i]
                for j in range(i, i + groupSize):
                    if freqs[j] < count:
                        return False
                    freqs[j] -= count
            return True
        return solutionFreqMap()