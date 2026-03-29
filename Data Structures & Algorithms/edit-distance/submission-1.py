from collections import deque



class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == 0:
            return len(word2)
        if len(word2) == 0:
            return len(word1)
        if word1 == word2:
            return 0

        # We can remove, add or replace a character in word1
        # But, since we don`t need to know which operations, just the amount of operations,
        # it is not different from changing mixed between word1 and word2 or just changing word2
        # Let`s force the smaller word being the word1
        if len(word1) > len(word2):
            word1, word2 = word2, word1

        lenDiff = len(word2) - len(word1)
        # Let's not touch common prefixes and sufixes, then we can work with smaller words
        L = 0
        for i in range(len(word1)):
            L = i
            if word1[i] != word2[i]:
                break
        if L > 0:
            word1 = word1[L:]
            word2 = word2[L:]

        R1 = len(word1)
        R2 = len(word2)
        for _ in range(R1):
            if word1[R1 - 1] != word2[R2 - 1]:
                break
            R1 -= 1
            R2 -= 1
        if R1 != len(word1):
            word1 = word1[:R1]
            word2 = word2[:R2]

        # Let's check if it can be easily solved with simple additions/removals,
        # i.e., if the character of the smallest are all in the biggest and in the same order
        i = j = 0
        print(word1, word2)
        while i < R1 and j < R2:
            print(i, j)
            if word1[i] == word2[j]:
                i += 1
            j += 1
        if i == R1:
            return lenDiff

        # Since need to know the minimum, a BFS over all meaningfuk operations would work better.
        add = rem = rep = 0
        # add - rem must be == lenDiff
        # Thus we MUST have a removal right after the first lenDiff additions and after any addition after that.
        maxOps = len(word2) # This is our cap of operations, this way we will not get into an infinite loop

        # Let's start with a bad solution
        # When do we need to remove a charcter from word1?
        #   When we need to shift the rest of the word to have a better matching
        #   e.g.: word1 = bcdef, word2 = cdefgh, in this case we remove, not replace
        # When an addition + a removal can be converted to a replace?
        #   When they occur at the same position, even if that position will be just in the future
        #   Thus it may be useful to record where the additions and removals happened compared to the original string
        L = 0
        # Let's work from left to right
        # I know a BFS would work better, but let's start with a DFS because it is easier to think that way and then convert to a BFS
        DP = {}
        def dfs(i, j):
            print(i, j, DP)
            if (i, j) in DP:
                return DP[(i, j)]
            if i == len(word1) and j == len(word2):
                DP[(i, j)] = 0
            elif i == len(word1):
                DP[(i, j)] = len(word2) - j
            elif j == len(word2):
                DP[(i, j)] = len(word1) - i
            elif word1[i] == word2[j]:
                # Skip this character
                DP[(i, j)] = dfs(i+1, j+1)
            else:
                # 3 possible operations, as we can also skip the character
                # Replace, we can move both to the next char in word1 word2
                rep = dfs(i + 1, j + 1)
                # removal, we can move to the next char in word1
                rem = dfs(i + 1, j)
                # Addition, we can move to the next char in word2
                add = dfs(i, j + 1)
                DP[(i, j)] = 1 + min(rep, rem, add)
            return DP[(i, j)]
        return dfs(0, 0)
        # What if we can improve the BFS with a 2D dinamic programming?
        # Each row represent the a state of the word1
        # Each col represents a position of the word1 being changed
        # Each cell represents the number of operations to get to to word2
        # We know the worst case is maxOps, which can be performed by replacing each char from word1 and add the remaining
        # Perhaps we could start with that case of maxOps, then remove the operations we don't need.
        # How to deal with the shifts?
        # 
        dp = [[maxOps]*maxOps for _ in maxOps]

        while word1 != word2:
            pass
            

        