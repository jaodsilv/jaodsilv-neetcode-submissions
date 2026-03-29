class Solution:
    def trap(self, height: List[int]) -> int:
        # Let's think on how much volume each index can hold
        # which is the min between the max to the left and the max to the right
        left = [height[0]]
        right = [height[-1]]
        for i in range(1, len(height)):
            left.append(max(left[-1], height[i]))
            right.append(max(right[-1], height[- i - 1]))

        right.reverse()
        return sum([min(L, R) - H for L, R, H in zip(left, right, height)])
        # volumes = [0]
        # for i in range(1, len(height) - 1):
        #     if height[i] == left[i] or height[i] == right[i]:
        #         volumes.append(0)
        #     else:
        #         volumes.append(min(left[i], right[i]) - height[i])
        # volumes.append(0)

        # totalVolume = sum
        # currVolume = 0
        # for v in volumes:
        #     if v == 0:
        #         maxVolume = max(maxVolume, currVolume)
        #         currVolume = 0
        #     else:
        #         currVolume += v
        # return maxVolume
