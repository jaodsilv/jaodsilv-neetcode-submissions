from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        # Let's count the number of cards of each value
        counter = dict(Counter(hand))
        maxi = max(counter.keys())
        mini = min(counter.keys())
        # print(f'min: {mini}')
        # print(f'max: {maxi}')
        # print(f'counter: {counter}')
        
        # Now we go from Mini to Maxi
        while counter:
            # First we find our next mini
            while mini not in counter:
                mini += 1
            # print(f'min: {mini}')
            # print(f'min + groupSize: {mini + groupSize}')
            if mini + groupSize - 1 > maxi:
                return False
            # Now we try to build a sequence,
            # while discarding any card that the count of unused cards gets to 0
            for i in range(mini, mini + groupSize):
                if i not in counter:
                    return False
                counter[i] -= 1
                if counter[i] == 0:
                    # print(f'Removing value: {i}')

                    del counter[i]
            # print(f'counter: {counter}')
        return True