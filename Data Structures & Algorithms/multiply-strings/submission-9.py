class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1[0] == '0' or num2[0] == '0':
            return '0'
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        
        dp = [[] for _ in range(10)]
        dp[0] = [0]
        num1List = [int(d) for d in num1][::-1]
        num2List = [int(d) for d in num2][::-1]

        def multiply_digit(digit: int, trail0s: int):
            if digit == 0:
                return 0
            if dp[digit]:
                return [0]*trail0s + dp[digit]
            res = []
            up = 0
            for d in num1List:
                up = digit*d + up
                res.append(up % 10)
                up //= 10
            if up:
                res.append(up)
            dp[digit] = res
            return [0]*trail0s + res
        def sum(A, B):
            if not B:
                return
            if len(A) < len(B):
                A.extend([0]*(len(B) - len(A)))
            up = 0
            for i in range(len(A)):
                a, b = A[i], B[i]
                up = a + b + up
                A[i] = up % 10
                up //= 10
            if up:
                A.append(up)
        res = []
        trail0s = 0
        for i in num2List:
            B = multiply_digit(i, trail0s)
            sum(res, B)
            trail0s += 1
        while res[-1] == 0:
            res.pop()
        return ''.join([str(d) for d in res][::-1])
