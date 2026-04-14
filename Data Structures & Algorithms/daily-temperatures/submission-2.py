class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 1:
            return [0]
        res = [-1]*len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            # print(stack, res)
            temp = temperatures[i]
            while stack and stack[-1][1] < temp:
                prev = stack.pop()
                res[prev[0]] = i - prev[0]

            stack.append((i, temp))

        for i in range(len(temperatures)):
            if res[i] == -1:
                res[i] = 0
        return res