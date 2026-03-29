class Solution:
    def trap(self, height: List[int]) -> int:
        # We are sure to look into local local maximums
        if len(height) <= 2:
            return 0
        
        i = 0
        # Ascending order
        while i < len(height) - 1 and height[i] < height[i+1]:
            i += 1
        if i == len(height) - 1:
            return 0

        total = 0
        curr = 0
        peaks = [i]

        # let`s first find all peaks
        for j in range(i + 2, len(height)):
            if height[j] > height[j-1] and (j == len(height) - 1 or height[j] > height[j + 1]):
                peaks.append(j)
        
        if len(peaks) == 1:
            return 0

        # Now let's filter those peaks to find the "recipients"
        left = i
        total = 0
        biggestAfter = []
        for j in peaks[::-1]:
            if not biggestAfter:
                biggestAfter.append(j)
            elif height[biggestAfter[-1]] < height[j]:
                biggestAfter.append(j)
            else:
                biggestAfter.append(biggestAfter[-1])
        biggestAfter.reverse()

        recipients = []
        for j in range(1, len(peaks)):
            if height[left] <= height[peaks[j]]:
                for k in range(left + 1, peaks[j]):
                    total += height[left] - height[k]
                left = peaks[j]
            elif biggestAfter[j] == peaks[j]: # and height[left] > height[peaks[j]]
                # Find actual leftie
                for k in range(left+1, peaks[j]):
                    if height[k] < height[peaks[j]]:
                        left = k - 1
                        break
                total += sum([height[peaks[j]] - height[k] for k in range(left + 1, peaks[j])])
                left = peaks[j]
        return total