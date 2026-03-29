from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # It's the same as finding the shortest path in a graph, which can be solved with a BFS
        # The challenge here is on building the graph
        if beginWord == endWord:
            return 1
        if endWord not in wordList:
            return 0

        def diff(word1, word2):
            hasDiff = False
            for c1, c2 in zip(word1, word2):
                if c1 != c2:
                    if hasDiff:
                        return False
                    hasDiff = True
            return True

            L = 0
            R = len(word1)
            i = len(word1) // 2
            print(f'word1: {word1}, word2: {word2}')
            def printAll(L, R, i):
                print(f'L: {L}, R: {R}, i: {i}')
                print(f'word1: {word1}, word2: {word2}, L: {L}, R: {R}, i: {i}')
                s = ""
                if i > 0:
                    s = f'word1[:{i}]: {word1[:i]}, word2[:{i}]: {word2[:i]}, '
                s = s + f'word1[{i}]: {word1[i]}, word2[{i}]: {word2[i]}'
                if i < len(word1) - 1:
                    s = s + f', word1[{i+1}:]: {word1[i+1:]}, word2[{i+1}:]: {word2[i+1:]}'
                print(s)
            dL = i == 0 or word1[:i] == word2[:i]
            dR = i == len(word1) - 1 or word1[i+1:] == word2[i+1:]
            dM = word1[i] == word2[i]
            # printAll(L, R, i)
            count = 5
            # Should stop if dM is false and either of the other two is False
            # Should stop if both not dL and not dR
            # Should stop if both not dM dL and dR are True, to return True
            while dM and (dL ^ dR):
                count -= 1
                if dL:
                    #Left side is equal, we move right
                    L = i
                    i = (L + R) // 2
                else:
                    R = i
                    i = (L + R) // 2
                dL = i == 0 or word1[:i] == word2[:i]
                dR = i == len(word1) - 1 or word1[i+1:] == word2[i+1:]
                dM = word1[i] == word2[i]
                # printAll(L, R, i)
            return dL and dR
        # print(diff('dot', 'cat'))
        # return 0
        # For each word we can replace each character with a * and find the neighbors
        notVisited = set(wordList)
        notVisited.discard(beginWord)
        notVisited.discard(endWord)
        L = {beginWord}
        R = {endWord}
        count = 1
        while L or R:
            print(f'count: {count}, L: {L}, R: {R}, notVisited: {notVisited}')
            if len(L & R) > 0:
                return 2 * count - 1
            for word1 in L:
                for word2 in R:
                    if diff(word1, word2):
                        return 2 * count
            count += 1
            notVisitedCopy = notVisited.copy()
            newL = set()
            for word1 in L:
                for word2 in notVisitedCopy:
                    if diff(word1, word2):
                        notVisited.discard(word2)
                        newL.add(word2)
            newR = set()
            for word1 in R:
                for word2 in notVisitedCopy:
                    if diff(word1, word2):
                        notVisited.discard(word2)
                        newR.add(word2)
            L = newL
            R = newR
        return 0
