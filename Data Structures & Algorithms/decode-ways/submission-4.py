class Solution:
    def numDecodings(self, s: str) -> int:
        # Let's start with examples
        if len(s) == 0 or s[0] == '0':
            return 0
        if len(s) == 1:
            return 1
        # If a digit is 0, it means the previous digit must be 1 or 2, otherwise it is invalid
        for i in range(len(s)):
            if s[i] == '0' and s[i - 1] != '2' and s[i - 1] != '1':
                return 0
        # Now we know it is valid

        fibs = [0] * (max(len(s) + 1, 4))
        fibs[0] = 1
        fibs[1] = 1
        fibs[2] = 2
        fibs[3] = 3
        def fib(n):
            if fibs[n] > 0:
                return fibs[n]
            res = fib(n-1) + fib(n-2)
            fibs[n] = res
            return res
        # If a digit is 1, it may be combined with the next one
        # If a digit is 2, it may be combined with the next one if it is less than or equal to 6

        # Let's divide into clusters of 12x
        clustersLens = []
        i = 0
        while i < len(s):
            # Move to the next 1 or 2
            while i < len(s) and s[i] not in '12':
                i += 1
            if i == len(s):
                break
            # Move to the end of the cluster and count. s[i] must be 1 or 2
            init = i
            while i < len(s) and s[i] in '12':
                i += 1
            if i == len(s):
                clustersLens.append(fib(i-init))
                break
            elif s[i] == '0':
                clustersLens.append(fib(i-1-init))
            elif s[i-1] == '1' or s[i] not in '789':
                clustersLens.append(fib(i-init+1))
            else: # s[i-1] == 2 and s[i] in '3456:
                clustersLens.append(fib(i-1-init))
        print(clustersLens)
        total = 1
        for i in clustersLens:
            total *= i
        return total
