import heapq

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Special tags
        if len(t) > len(s):
            return ""
        if len(t) == 1:
            return t if t in s else ""

        count = {}
        for c in t:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1

        # Use a MAX heap to know when the maximum count got to 0
        countHeap = [(v, k) for k, v in count.items()]
        heapq.heapify_max(countHeap)
        # Now lets do use a sliding window of variable size
        l = r = 0
        shortest = s + 'a'
        while r < len(s):
            # print(l, r, s[l:r], count, countHeap)
            if countHeap[0][0] > 0:
                c = s[r]
                if c in count:
                    count[c] -= 1
                    if c == countHeap[0][1]:
                        heapq.heapreplace_max(countHeap, (count[c], c))
                        c = countHeap[0][1]
                        while countHeap[0][0] != count[c]:
                            heapq.heapreplace_max(countHeap, (count[c], c))
                            c = countHeap[0][1]
                    else:
                        heapq.heappush_max(countHeap, (count[c], c))
                r += 1
            if countHeap[0][0] <= 0 or r - l >= len(shortest):
                if countHeap[0][0] == 0 and r - l < len(shortest):
                    shortest = s[l:r]
                c = s[l]
                if c in count:
                    count[c] += 1
                    if count[c] > countHeap[0][0] and c == countHeap[0][1]:
                        heapq.heapreplace_max(countHeap, (count[c], c))
                    else:
                        heapq.heappush_max(countHeap, (count[c], c))
                l += 1

        while countHeap[0][0] <= 0 and l < r:
            # print(l, r, s[l:r], count, countHeap)
            if countHeap[0][0] == 0 and r - l < len(shortest):
                shortest = s[l:r]
            c = s[l]
            if c in count:
                count[c] += 1
                if count[c] > countHeap[0][0]:
                    if c == countHeap[0][1]:
                        heapq.heapreplace_max(countHeap, (count[c], c))
                    else:
                        heapq.heappush_max(countHeap, (count[c], c))
            l += 1
        # print(l, r, s[l:r], count, countHeap)

        return shortest if len(shortest) <= len(s) else ""


