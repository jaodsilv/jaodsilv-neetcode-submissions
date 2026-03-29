class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n > 1:
            if n in visited:
                return False
            visited.add(n)

            newN = 0
            while n:
                newN += (n % 10)**2
                n //= 10
            n = newN
        return True