from collections import deque, defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # It's the same as finding the shortest path in a graph, which can be solved with a BFS
        # The challenge here is on building the graph
        if beginWord == endWord:
            return 1
        if endWord not in wordList:
            return 0

        def diff(word1, word2):
            # hasDiff = False
            # for c1, c2 in zip(word1, word2):
            #     if c1 != c2:
            #         if hasDiff:
            #             return False
            #         hasDiff = True
            # return True

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
                    word1 = word1[i+1:]
                    word2 = word2[i+1:]
                    i = len(word1) // 2
                else:
                    word1 = word1[:i]
                    word2 = word2[:i]
                    R = i
                    i = len(word1) // 2
                dL = i == 0 or word1[:i] == word2[:i]
                dR = i == len(word1) - 1 or word1[i+1:] == word2[i+1:]
                dM = word1[i] == word2[i]
                # printAll(L, R, i)
            return dL and dR
        # print(diff('dot', 'cat'))
        # return 0
        # For each word we can replace each character with a * and find the neighbors
        def patterns(word):
            return {word[:i] + '*' + word[i+1:] for i in range(len(word))}
        nei = defaultdict(list)
        for word in wordList:
            if word == beginWord or word == endWord:
                continue
            for pattern in patterns(word):
                nei[pattern].append(word)
        L = {beginWord}
        R = {endWord}
        count = 1
        while L or R:
            print(f'count: {count}, L: {L}, R: {R}')
            if len(L & R) > 0:
                return 2 * count - 1
            for word1 in L:
                for word2 in R:
                    if diff(word1, word2):
                        return 2 * count
            count += 1
            newL = set()
            for word1 in L:
                for pattern in patterns(word1):
                    for word2 in nei[pattern]:
                        newL.add(word2)
                    nei[pattern] = []
            newR = set()
            for word1 in R:
                for pattern in patterns(word1):
                    for word2 in nei[pattern]:
                        newR.add(word2)
                    nei[pattern] = []
            L = newL
            R = newR
        return 0
