class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        fuel = 0
        init = -n
        for i in range(-n, n):
            if i == init + n:
                return init + n
            fuel += gas[i] - cost[i]
            if fuel < 0:
                if i >= 0:
                    return -1
                init = i + 1
                fuel = 0
        return -1
