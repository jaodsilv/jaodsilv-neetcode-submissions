class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # We can compute the minimum cost to get TO a specific floor
        totalCost = [0] * (len(cost) + 1)
        for i in range(2, len(cost) + 1):
            totalCost[i] = min(totalCost[i-1] + cost[i-1], totalCost[i-2] + cost[i-2])
        return totalCost[-1]