class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        Stack
        '''
        stack = []
        res = 0
        for i, h in enumerate(height):
            while stack and h > stack[-1][1]:
                # (i, h) is a right wall
                j, bottom = stack.pop()
                if stack:
                    res += (min(h, stack[-1][1]) - bottom) * (i - stack[-1][0] - 1)
            stack.append((i, h))
            # print("i", i, "h", h, "stack", stack, "res", res)
        return res

        '''
        Prev Solution
        # We are sure to look into local local maximums
        if len(height) <= 2:
            return 0
        
        i = 0
        # Ascending order
        while i < len(height) - 1 and height[i] < height[i+1]: # O(n)
            i += 1
        if i == len(height) - 1:
            return 0

        total = 0
        curr = 0
        peaks = [i]

        # let`s first find all peaks
        for j in range(i + 2, len(height)): # O(n)
            if height[j] > height[j-1] and (j == len(height) - 1 or height[j] > height[j + 1]):
                peaks.append(j)
        
        if len(peaks) == 1:
            return 0
        '''

        # Now let's filter those peaks to find the "recipients"
        left = i
        total = 0
        biggestAfter = []
        for j in peaks[::-1]: # O(n) as we have at most n // 2 peaks
            if not biggestAfter:
                biggestAfter.append(j)
            elif height[biggestAfter[-1]] < height[j]:
                biggestAfter.append(j)
            else:
                biggestAfter.append(biggestAfter[-1])
        biggestAfter.reverse()

        recipients = []
        for j in range(1, len(peaks)): # O(#peaks)
            if height[left] <= height[peaks[j]]:
                for k in range(left + 1, peaks[j]): # O(interval betweeen a peak)
                    total += height[left] - height[k]
                left = peaks[j]
            elif biggestAfter[j] == peaks[j]: # and height[left] > height[peaks[j]]
                # Find actual leftie
                for k in range(left+1, peaks[j]): # O(interval betweeen a peak)
                    if height[k] < height[peaks[j]]:
                        left = k - 1
                        break
                total += sum([height[peaks[j]] - height[k] for k in range(left + 1, peaks[j])]) # O(interval betweeen a peak)
                left = peaks[j]
            # O(Total) = O(#peaks)*O(interval between peaks) = O(n)
        return total