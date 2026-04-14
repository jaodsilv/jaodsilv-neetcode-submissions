class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 1:
            return [0]
        res = {}
        stack = []
        for i in range(len(temperatures)):
            # print(stack, res)
            temp = temperatures[i]
            while stack and stack[-1][1] < temp:
                prev = stack.pop()
                res[prev[0]] = i - prev[0]

            stack.append((i, temp))

        result = []
        for i in range(len(temperatures)):
            if i in res:
                result.append(res[i])
            else:
                result.append(0)
        return result