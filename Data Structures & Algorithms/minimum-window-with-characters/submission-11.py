import heapq

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Special tags
        if len(t) > len(s):
            return ""
        if len(t) == 1:
            return t if t in s else ""

        count = {}
        maximum = 0
        for c in t:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
            maximum = max(maximum, count[c])

        bucketSorted = [set() for _ in range(maximum + 1)]

        for k, v in count.items():
            bucketSorted[v].add(k)

        # Use a MAX heap to know when the maximum count got to 0
        # Now lets do use a sliding window of variable size
        l = r = 0
        shortest = s + 'a'
        while r < len(s):
            # print(l, r, s[l:r], count, countHeap)
            if maximum > 0:
                c = s[r]
                if c in count:
                    if count[c] > 0:
                        bucketSorted[count[c]].discard(c)
                        if len(bucketSorted[maximum]) == 0:
                            maximum -= 1
                    count[c] -= 1
                    if count[c] >= 0:
                        bucketSorted[count[c]].add(c)
                r += 1
            if maximum == 0 or r - l >= len(shortest):
                if maximum == 0 and r - l < len(shortest):
                    shortest = s[l:r]
                c = s[l]
                if c in count:
                    if count[c] >= 0:
                        bucketSorted[count[c]].discard(c)
                    count[c] += 1
                    if count[c] > 0:
                        bucketSorted[count[c]].add(c)
                        maximum = max(maximum, count[c])
                l += 1

        while maximum == 0 and l < r:
            # print(l, r, s[l:r], count, countHeap)
            if r - l < len(shortest):
                shortest = s[l:r]
            c = s[l]
            if c in count:
                if count[c] == 0:
                    break
                count[c] += 1
            l += 1
        # print(l, r, s[l:r], count, countHeap)

        return shortest if len(shortest) <= len(s) else ""


