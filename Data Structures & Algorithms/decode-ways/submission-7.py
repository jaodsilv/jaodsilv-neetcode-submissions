class Solution:
    def intToChar(i):
        pass
    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 0

        #Check if it is a valid sequence
        if s[0] == 0:
            return 0


        def dfs(i, mem):
            if i >= len(s):
                return 1

            if mem[i] > 0:
                return mem[i]


            if i == len(s) - 1:
                if s[-1] != '0':
                    mem[-1] = 1
                    return 1
                else:
                    mem[-1] = 0
                    return 0
            if s[i] == '0':
                mem[i] = 0
                return 0
            elif s[i] == '1':
                mem[i] = dfs(i+1, mem) + dfs(i+2, mem)
                return mem[i]
            elif s[i] == '2' and s[i+1] in '0123456':
                mem[i] = dfs(i+1, mem) + dfs(i+2, mem)
                return mem[i]
            mem[i] = dfs(i+1, mem)
            return mem[i]

        mem = [0]*len(s)
        return dfs(0, mem)
