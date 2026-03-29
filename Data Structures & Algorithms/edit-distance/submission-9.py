class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # let's eliminate equal prefixes and suffixes
        for i in range(min(len(word1), len(word2))):
            if word1[i] != word2[i]:
                word1 = word1[i:]
                word2 = word2[i:]
                break

        for i in range(1, min(len(word1), len(word2))):
            if word1[-i] != word2[-i]:
                if i > 1:
                    word1 = word1[:-i+1]
                    word2 = word2[:-i+1]
                break

        # Second let's handle special cases
        if len(word1) == 0:
            return len(word2)
        if len(word2) == 0:
            return len(word1)

        # Now it is guaranteed the length of each is at least 1.
        if len(word1) == 1:
            if word1[0] in word2:
                return len(word2) - 1
            else:
                return len(word2)
        if len(word2) == 1:
            if word2[0] in word1:
                return len(word1) - 1
            else:
                return len(word1)

        # Now it is guaranteed the length of each is at least 2.
        # We could use a prefix tree
        # Also a dfs over the diff
        # Or a DP over the differences
        # Let's go with DP
        if len(word1) > len(word2):
            word1, word2 = word2, word1
        def newDP(i):
            return [0]*len(word1)+[i]
        dpPrev = [len(word1)-i for i in range(len(word1))] + [0]
        print(dpPrev)
        # max changes is = max(len(word1), len(word2))
        # There are 4 types of decisions: add, remove, change, or do nothing 
        for i in range(len(word2)-1,-1,-1):
            dp = newDP(len(word2)-i)
            for j in range(len(word1)-1,-1,-1):
                if word1[j] == word2[i]:
                    dp[j] = dpPrev[j+1]
                else:
                    dp[j] = min(dpPrev[j+1], dpPrev[j], dp[j+1]) + 1
            dpPrev = dp
            print(dpPrev)

        print(word1)
        print(word2)
        # print(dpPrev)

        return dpPrev[0]
        '''
             d         t         c         o     d -
        a 1C1R1A|3C 2R1A|1R2C 3r1a      3R1C    4R 5R
        t 1R2A|2C1A 1R1A|2C   2r1a|1R2C 2R1C    3R 4R
        c 1R3A|2C2A 1R2A|2C1A 1r1a|2C   1R1C    2R 3R
        d 1R4A|2C3A 1R3A|2C2A 1R2A|1A2C 1R1A|2C 1R 2R
        e   1C4A      1C3A      1c2a      1C1A  1C 1R
        -   5A        4A        3A        2A    1A  0

           e  y  -
        k [3, 3, 4]
        e [2, 2, 3]
        y [1, 1, 2]
        s [2, 1, 1]
        - [2, 1, 0]


        If different:
        min of:
        +1C (from diag)

        ~-1A+1C (from down)~
        +1R (from down)

        +1A (from right)
        ~-1R+1C (from right)~

        If equals
        ==NO CHANGE (from diag)==

        -1A (from down)
        -1C+1R (from down)

        -1C+1A (from right)
        -1R+1C (from right)
             i n t e n
        e   [4, 3, 3, 3, 4, 4]
        x   [4, 3, 2, 2, 3, 3]
        e   [4, 3, 2, 1, 2, 2]
        c   [4, 3, 2, 2, 1, 1]
        u   [4, 3, 2, 1, 1, 0]
        -   [5, 4, 3, 2, 1, 0]
        '''