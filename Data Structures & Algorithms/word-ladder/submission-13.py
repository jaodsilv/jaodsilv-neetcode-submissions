from collections import deque, defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # It's the same as finding the shortest path in a graph, which can be solved with a BFS
        # The challenge here is on building the graph
        if beginWord == endWord:
            return 1
        if endWord not in wordList:
            return 0

        nei = defaultdict(list)
        patterns = {}
        patterns[beginWord] = [beginWord[:i] + '*' + beginWord[i+1:] for i in range(len(beginWord))]
        for word in wordList:
            patterns[word] = [word[:i] + '*' + word[i+1:] for i in range(len(word))]
            if word == beginWord or word == endWord:
                continue
            for pattern in patterns[word]:
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
                    if word1 == 'bat' and word2 == 'dag':
                        print(patterns[word1])
                        print(patterns[word2])
                    for p1, p2 in zip(patterns[word1], patterns[word2]):
                        if p1 == p2:
                            return 2 * count
            count += 1
            newL = set()
            for word1 in L:
                for pattern in patterns[word1]:
                    for word2 in nei[pattern]:
                        if word2 != word1:
                            newL.add(word2)
                    nei[pattern] = []
            newR = set()
            for word1 in R:
                for pattern in patterns[word1]:
                    for word2 in nei[pattern]:
                        if word2 != word1:
                            newR.add(word2)
                    nei[pattern] = []
            L = newL
            R = newR
        return 0
