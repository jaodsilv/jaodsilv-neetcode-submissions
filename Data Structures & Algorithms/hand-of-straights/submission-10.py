from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        # Let's count the number of cards of each value
        handSet = set(hand) # O(n)
        counter = dict(Counter(hand))  # O(n)
        
        # Now we find contiguous values
        # In these 2 while loops, each element from the contiguous range will be visited at most ONCE.
        # which is bound to SUM(O(range length) + O(elements in range))
        # = SUM(O(elements in range)) + SUM(O(range length))  total
        # = O(n) + O(distinct(n)) = O(n) total
        while handSet:  # O(??)
            # First we find our next mini
            base = handSet.pop()  # O(1)
            mini = base
            # In these 2 while loops, each element from the contiguous range will be visited at most ONCE.
            # which is bound to O(range length) total
            while mini - 1 in handSet:  # O(range length)
                mini -= 1
                handSet.discard(mini) # O(1)

            maxi = base
            while maxi + 1 in handSet:  # O(range length)
                maxi += 1
                handSet.discard(maxi) # O(1)
            
            # print(f'min: {mini}')
            # print(f'min + groupSize: {mini + groupSize}')
            if mini + groupSize - 1 > maxi:
                return False
            # Now we try to build a sequence,
            # while discarding any card that the count of unused cards gets to 0
            # Each element from the contiguous range will be visited at most it count number of times.
            # which is bound to O(elements in range) total
            while mini in counter:
                newMiniSet = False
                for i in range(mini, mini + groupSize):  # O(groupSize)
                    if i not in counter:
                        print(f'i not in counter: {i}, {counter}')
                        return False
                    counter[i] -= 1
                    if counter[i] == 0:
                        del counter[i]  # O(1)
                    elif not newMiniSet:
                        newMiniSet = True
                        mini = i
                        # print(f'Removing value: {i}')
                if not newMiniSet:
                    mini += groupSize
            if mini != maxi + 1:
                print(f'mini: {mini}, maxi: {maxi}, maxi - groupSize + 1 = {maxi - groupSize + 1}')
                return False

                # print(f'counter: {counter}')
        return True