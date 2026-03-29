class Solution:
    def trap(self, height: List[int]) -> int:
        # Let's think on how much volume each index can hold
        # which is the min between the max to the left and the max to the right
        left = [height[0]]
        right = [height[-1]]
        # O(n) time and space
        for i in range(1, len(height)):
            left.append(max(left[-1], height[i]))
            right.append(max(right[-1], height[- i - 1]))

        right.reverse()
        # O(n) time and space
        total = 0
        for L, R, H in zip(left, right, height):
            total += min(L, R) - H
        return total
