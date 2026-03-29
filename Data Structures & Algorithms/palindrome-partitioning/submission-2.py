class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = [list(s)]

        def isPalindrome(a):
            for i in range(len(a) // 2):
                if a[i] != a[-i-1]:
                    return False
            return True

        def bruteForce():
            # Find ALL palindromes
            palindromes = defaultdict(list) # Stores the palindromes starting at an specific index
            for i in range(len(s)):
                for j in range(min(i + 1, len(s) - i)):
                    if s[i-j] == s[i+j]:
                        palindromes[i-j].append(i + j)
                    else:
                        break
                for j in range(min(i + 1, len(s) - i - 1)):
                    if s[i - j] == s[i + j + 1]:
                        palindromes[i-j].append(i + j + 1)
                    else:
                        break

            # Now we create the possible combinations based on the first palindrome
            dp = [[] for _ in range(len(s) + 1)]
            dp[-1] = [[]]

            def dfs(i):
                if dp[i]:
                    return dp[i]
                if i == len(s):
                    return []
                if i not in palindromes:
                    return None
                for j in palindromes[i]:
                    tmp = dfs(j + 1)
                    if tmp:
                        for comb in tmp:
                            dp[i].append([s[i:j+1]] + comb)
                return dp[i]


            res = dfs(0)
            return res if res is not None else []

            # for i in range(len(s)-1, -1, -1):
            #     for j in palindromes[i]:
            #         if dp[j+1] == None:
            #             continue

            #         for comb in dp[j+1]:
            #             dp[i].append([s[i:j+1]] + comb)


            # return dp[0]
        return bruteForce()