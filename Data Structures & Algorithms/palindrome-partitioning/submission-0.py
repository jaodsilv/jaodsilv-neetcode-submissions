# from collections import deque
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        '''
        Since we want to build the palindromes with ALL elements, then we can go one by one
        Then repeate the processto each different solution
        '''
        res = []

        # First let's find all possible substrings that make palindromes
        pals = []
        for i in range(len(s)):
            # Test with i being the center
            j = i
            k = i
            while j >= 0 and k < len(s) and s[j] == s[k]:
                pals.append((j, k))
                j -= 1
                k += 1

            j = i
            k = i + 1
            # Test with i and i+1 being the center
            while j >= 0 and k < len(s) and s[j] == s[k]:
                pals.append((j, k))
                j -= 1
                k += 1

        pals.sort(key=lambda x: x[0])
        # Now we have to build all possible partitionings

        # let's do it recursively
        def dfs(i, left, curr):
            if left == len(s):
                # print(f'curr={curr}')
                res.append(curr.copy())
                return

            for j in range(i, len(pals)):
                # print(f'pals[j][0] == left: {pals[j][0]} == {left}; j = {j}')
                if pals[j][0] == left:
                    curr.append(pals[j])
                    dfs(j + 1, pals[j][1] + 1, curr)
                    curr.pop()
                elif pals[j][0] > left:
                    return

        # print(pals)
        for i in range(len(pals)):
            # print(f'i={i}')
            if pals[i][0] > 0:
                # print(res)
                return [[s[y[0]:y[1] + 1] for y in x] for x in res]
            # print(f'dfs(i + 1, pals[i][1] + 1, [pals[i]])=dfs({i + 1}, {pals[i][1] + 1}, [{pals[i]}])')
            dfs(i + 1, pals[i][1] + 1, [pals[i]])

        # print(res)
        return [[s[y[0]:y[1] + 1] for y in x] for x in res]