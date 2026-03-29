class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        def twoLoopSolution():
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

        def twoPointersSolution():
            fuel = 0
            start = 0
            end = 0
            while start > -n and end < n  and start + n != end:
                print(start, end, fuel)
                if fuel >= 0:
                    fuel += gas[end] - cost[end]
                    end += 1
                else: # fuel < 0
                    start -= 1
                    fuel += gas[start] - cost[start]
            print(start, end, fuel)
            if start + n != end or fuel < 0:
                return -1
            else:
                return end if end < n else 0
        # return twoLoopSolution()
        return twoPointersSolution()
