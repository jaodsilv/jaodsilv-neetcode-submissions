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

        print(peaks)
        # Now let's filter those peaks to find the "recipients"
        left = i

        total = 0

        biggestAfter = []
        lastBiggestBefore = []
        for j in peaks[::-1]:
            if not biggestAfter:
                biggestAfter.append(j)
            elif height[biggestAfter[-1]] < height[j]:
                biggestAfter.append(j)
            else:
                biggestAfter.append(biggestAfter[-1])
        biggestAfter.reverse()
        print(biggestAfter)

        recipients = []
        for j in range(1, len(peaks)):
            if height[left] <= height[peaks[j]]:
                for k in range(left + 1, peaks[j]):
                    total += height[left] - height[k]
                left = peaks[j]
            else: #height[left] > height[peaks[j]]
                if biggestAfter[j] == peaks[j]:
                    # Find actual leftie
                    for k in range(left+1, peaks[j]):
                        if height[k] < height[peaks[j]]:
                            left = k - 1
                            break
                    total += sum([height[peaks[j]] - height[k] for k in range(left + 1, peaks[j])])
                    left = peaks[j]
                else:
                    continue
                # Should I continue or compute?
                # Case 1 [...,5,0,3,0,4...] # one of the following peaks is bigger than this
                # Case 2 [...,5,0,3,0,2...] # The follo
                # Case 3 [...,5,0,3,0,2,0] # Last peak
        #         recipients.append((peaks[0], peaks[1]))
        #     if height[j] < height[right]:

        #     if height[j] > height[right]:
        #         right = j
            



        # j = i + 1
        # currs = [0]*len(height)


        # # Examples:
        # #   [4,3,2,1,0]
        # #   [0,1,2,0,0,5,0,4,0,2,4,5]
        # while j < len(height):
        #     print(f'i={i},j={j},peaks={peaks}')
        #     # if j == len(height) - 1:
        #     #     if height[-1] < height[-2]:
        #     #         return total
        #     #     while peaks and height[-1] > height[peaks[-1]]:
        #     #         lastpeak = peaks.pop()
        #     #         blockAbove = (j - lastpeak - 1) * (height[-1] - height[lastpeak])
        #     #         total += curr-blockAbove
        #     #         curr = blockAbove
        #     #         print(f'total={total},curr={curr}')
        #     #     if peaks:
        #     #         if height[-1] == height[peaks[-1]]:
        #     #             blockAbove = (j - i - 1) * (height[-1] - height[lastpeak])
        #     #             total += curr
        #     #         else:
        #     #             curr = 0
        #     #             for i in range()
        #     #     return total
        #     # el
        #     if height[j] >= height[i]:
        #         total += curr
        #         curr = 0
        #         print(f'total={total},curr={curr}')
        #         i = j
        #         # Stop at the next peak
        #         while i < len(height) - 1 and height[i] < height[i+1]:
        #             i += 1
        #         if i == len(height) - 1:
        #             return total
        #         peaks = [i]
        #         j = i + 1
        #     else: # height[j] < height[i]:
        #         if height[j] > height[j-1] and (j == len(height) - 1 or height[j] > height[j+1]):
        #             print("is Peak, j", j)
        #             # Find the last element which is above the current element
        #             # We know already it is lower than the previous peak, which means there is no peak between them
        #             # and it means it half monotonic down, monotonic up
        #             lastpeak = i
        #             while height[j] > height[peaks[-1]]:
        #                 lastpeak = peaks.pop()
        #                 totalAbove = currs[lastpeak] + (j - lastpeak - 1) * (height[i] - height[j])
        #                 total += curr - totalAbove
        #                 curr = totalAbove
        #             if height[j] == height[peaks[-1]]:
        #                 lastpeak = peaks.pop()
        #                 totalAbove = currs[lastpeak] + (j - lastpeak - 1) * (height[j] - height[i])
        #                 total += curr - totalAbove
        #                 curr = totalAbove
        #             else:
        #                 print(peaks)
        #                 lastpeak = peaks[-1]
        #                 totalPrev = currs[lastpeak]
        #                 pos = peaks[-1] + 1
        #                 for k in range(peaks[-1] + 1, lastpeak):
        #                     if height[k] < height[j]:
        #                         pos = k - 1
        #                         break
        #                     currs[k] = currs[k-1] + height[i] - height[k]
        #                 print('pos', pos)
        #                 totalAbove = currs[pos] + (height[i] - height[pos]) * (j - pos - 1)
        #                 total += curr - totalAbove
        #                 curr = totalAbove
        #         curr += height[i] - height[j]
        #         currs[j] = curr
        #         print(f'total={total},curr={curr}')
        #         j += 1
        return total