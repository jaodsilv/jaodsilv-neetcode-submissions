import heapq

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge cases>
        if len(t) > len(s):
            return ""

        if len(t) == 1:
            return t if t in s else ""
        
        # First let's count t
        counter = {} # O(52) = O(1)

        for c in t:
            if c in counter:
                counter[c] += 1
            else:
                counter[c] = 1

        heap = [(v, k) for k, v in counter.items()]
        heapq.heapify_max(heap)

        print('0:', counter, heap)
        # Count the first group, then we follow with a variable window
        for i in range(len(t)):
            c = s[i]
            if c in counter:
                counter[c] -= 1
                # Only updates heap when there is chance of change in the top value
                while heap[0][0] != counter[heap[0][1]]:
                    heapq.heapreplace_max(heap, (counter[heap[0][1]], heap[0][1]))
        print('1:', counter, heap)
        
        if heap[0][0] == 0:
            return s[:len(t)]

        L = 0
        R = len(t)
        minS = ""
        minSize = len(s) + 1

        # print(L, R)
        # count = 10
        while R < len(s):# and count:
            # count -= 1
            cL = s[L]
            print('2:', L, R, cL, minSize, counter, minS)
            while L < R and (R - L >= minSize or cL not in counter or counter[cL] < 0):
                print('12:', minS)
                L += 1
                if cL in counter:
                    counter[cL] += 1
                    if counter[cL] > heap[0][0]:
                        if heap[0][1] == cL:
                            heap[0] = (counter[cL], cL)
                        else:
                            heapq.heappush_max(heap, (counter[cL], cL))
                cL = s[L]
            if heap[0][0] <= 0 and L != R and R - L < minSize:
                minS = s[L:R]
                minSize = R - L
                print('13:', minS)
            else:
                print('3:', L, R, counter, heap, minS)
            if R < len(s) and heap[0][0] > 0:
                while R < len(s) and heap[0][0] > 0: # heap[0][0] = 0
                    cR = s[R]
                    print('4:', cR, R, minS)
                    if cR in counter:
                        print('5: cR in counter')
                        counter[cR] -= 1
                        while heap[0][0] != counter[heap[0][1]]:
                            print('14: update heap top')
                            heapq.heapreplace_max(heap, (counter[heap[0][1]], heap[0][1]))
                        print("6:", R, L, heap, counter, minS)
                    R += 1 # R = 3
                if heap[0][0] == 0 and R - L < minSize:
                    minSize = R - L
                    minS = s[L:R]
                    print('15:', heap, R, L, minSize, counter, minS)
            else:
                print('7:', heap, R, L, minSize, minS)
                # R += 1
            if heap[0][0] == 0 and R - L + 1 < minSize: 
                print('8:', heap, R, L, minSize, minS)
                minSize = R - L + 1
                minS = s[L:R+1]
            else:
                print('9:', minS)
            print('10:', L, R, counter, heap, s[L:R], minS)
        cL = s[L]
        while L < R and (R - L > minSize or cL not in counter or counter[cL] < 0):
            L += 1
            if cL in counter:
                counter[cL] += 1
                if counter[cL] > heap[0][0]:
                    if heap[0][1] == cL:
                        heap[0] = (counter[cL], cL)
                    else:
                        heapq.heappush_max(heap, (counter[cL], cL))
            cL = s[L]
        
        print('11:', L, R, counter, heap, s[L:R])
        if heap[0][0] <= 0 and R-L < minSize:
            minS = s[L:R]
        return minS

                            

