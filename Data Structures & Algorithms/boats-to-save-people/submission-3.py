# import bisect
from bisect import bisect_left
from collections import Counter #,defaultdict
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # We have to distribute as evenly as possible
        # Or we may test for a number of boats

        people.sort()
        # counter = Counter(people)
        # weights = sorted(counter.keys())

        # Since each boar can carry only 2 person we may use a binary search or a 2 pointers to find the complimentary.
        count = 0
        # Eliminating those that can be paired at all
        # while people[-1] == limit:
        #     count += 1
        #     people.pop()
        L, R = 0, len(people)-1
        while L < R:
            count += 1
            if people[L] + people[R] <= limit:
                L += 1
            R -= 1
        if L == R:
            count += 1
        return count