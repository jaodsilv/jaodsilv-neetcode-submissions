class Solution:
    def climbStairs(self, n: int) -> int:
        # I can recurse over the previous solutions and build over them
        # Like a fibonacci, it is the sum of self.climbStairs(n - 1) + self.climbStairs(n - 2)
        if n <= 1:
            return 1
        if n == 2:
            return 2

        fibs = [0] * 30
        fibs[0] = 1
        fibs[1] = 2
        def fib(n):
            if fibs[n-1] == 0:
                return fib(n-1) + fib(n-2)
            else:
                return fibs[n-1]
        return fib(n)