from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        # Let's count the number of cards of each value
        handSet = set(hand)
        counter = dict(Counter(hand))
        # print(f'min: {mini}')
        # print(f'max: {maxi}')
        # print(f'counter: {counter}')
        
        # Now we find contiguous values
        while handSet:
            # First we find our next mini
            base = handSet.pop()
            mini = base
            while mini - 1 in handSet:
                mini -= 1
                handSet.discard(mini)

            maxi = base
            while maxi + 1 in handSet:
                maxi += 1
                handSet.discard(maxi)
            
            # print(f'min: {mini}')
            # print(f'min + groupSize: {mini + groupSize}')
            if mini + groupSize - 1 > maxi:
                return False
            # Now we try to build a sequence,
            # while discarding any card that the count of unused cards gets to 0
            while mini in counter:
                newMiniSet = False
                for i in range(mini, mini + groupSize):
                    if i not in counter:
                        print(f'i not in counter: {i}, {counter}')
                        return False
                    counter[i] -= 1
                    if counter[i] == 0:
                        del counter[i]
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