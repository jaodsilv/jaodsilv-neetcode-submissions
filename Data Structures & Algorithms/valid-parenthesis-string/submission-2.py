from collections import Counter
class Solution:
    def checkValidString(self, s: str) -> bool:
        counter = Counter(s)
        stars = counter['*']
        opens = counter['(']
        closes = counter[')']
        if abs(closes-opens) > stars:
            return False

        # We can use opens and closes as a number
        # It cannot be negative ever, `(` does a +1, and a `)` does -1
        memo = {}
        def dfs(opened, i):
            if (opened, i) in memo:
                return memo[(opened, i)]
            if i == len(s):
                return opened == 0
            if opened < 0:
                return False
            if s[i] == '(':
                memo[(opened, i)] = dfs(opened + 1, i + 1)
            elif s[i] == ')':
                memo[(opened, i)] = dfs(opened - 1, i + 1)
            else:
                memo[(opened, i)] = dfs(opened + 1, i + 1) or dfs(opened - 1, i + 1) or dfs(opened, i + 1)
            return memo[(opened, i)]
        return dfs(0, 0)
