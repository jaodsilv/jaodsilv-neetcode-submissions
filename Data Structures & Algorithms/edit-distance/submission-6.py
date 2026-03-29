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
        dp = [[[0,0,0] for _ in range(len(word1))]+[[0,0,len(word2)-i]] for i in range(len(word2))]
        dp.append([[len(word1)-i, 0, 0] for i in range(len(word1))] + [[0,0,0]])

        # max changes is = max(len(word1), len(word2))
        # There are 4 types of decisions: add, remove, change, or do nothing 
        for i in range(len(word2) - 1, -1, -1):
            for j in range(len(word1) - 1, -1, -1):
                if word1[j] == word2[i]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    Ad, Cd, Rd = dp[i+1][j+1]
                    Cd+=1
                    Sd = Ad + Cd + Rd
                    Ab, Cb, Rb = dp[i+1][j]
                    Rb += 1
                    Sb = Ab + Cb + Rb
                    Ar, Cr, Rr = dp[i][j+1]
                    Ar+=1
                    Sr = Ar + Cr + Rr
                    if min(Sd, Sb, Sr) == Sd:
                        dp[i][j] = [Ad, Cd, Rd]
                    elif min(Sd, Sb, Sr) == Sb:
                        dp[i][j] = [Ab, Cb, Rb]
                    else: #  min(Sd, Sb, Sr) == Sr:
                        dp[i][j] = [Ar, Cr, Rr]

        print(word1)
        print(word2)
        print(dp)

        return sum(dp[0][0])
        '''
             d         t         c         o     d -
        a 1C1R1A|3C 2R1A|1R2C 3r1a      3R1C    4R 5R
        t 1R2A|2C1A 1R1A|2C   2r1a|1R2C 2R1C    3R 4R
        c 1R3A|2C2A 1R2A|2C1A 1r1a|2C   1R1C    2R 3R
        d 1R4A|2C3A 1R3A|2C2A 1R2A|1A2C 1R1A|2C 1R 2R
        e   1C4A      1C3A      1c2a      1C1A  1C 1R
        -   5A        4A        3A        2A    1A  0

              e      y  -
        k   2R1C    3R 4R
        e   1R1C    2R 3R
        y   1R1A|2C 1R 2R
        s    1C1A   1C 1R
        -      2A   1A 0

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
              a            t            c              d        e            -
        e   [0, 2, 0],   [0, 1, 1],   [0, 1, 2],   [0, 1, 3], OK[0, 0, 4], [0, 0, 5]
        t   [1, 1, 0],   [0, 1, 0],   [0, 1, 1],   [0, 1, 2], OK[0, 1, 3], [0, 0, 4]
        c   [2, 1, 0],   [1, 1, 0],   [0, 1, 0],   [0, 1, 1], OK[0, 1, 2], [0, 0, 3]
        o   [3, 1, 0],   [2, 1, 0],   [1, 1, 0], NOT[0, 1, 0],OK[0, 1, 1], [0, 0, 2]
        d   [4, 0, 0],   [3, 0, 0],   [2, 0, 0],  OK[1, 0, 0], OK[0, 1, 0], [0, 0, 1]
        -   [5, 0, 0],   [4, 0, 0],   [3, 0, 0],   [2, 0, 0],   [1, 0, 0], [0, 0, 0]]]
        '''