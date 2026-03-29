from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # It's the same as finding the shortest path in a graph, which can be solved with a BFS
        # The challenge here is on building the graph
        if beginWord == endWord:
            return 1
        if endWord not in wordList:
            return 0

        # For each word we can replace each character with a * and find the neighbors
        notVisited = set(wordList)
        notVisited.discard(beginWord)
        queue = deque([beginWord])
        count = 1
        while queue:
            print(f'queue: {queue}')
            count += 1
            for _ in range(len(queue)):
                word1 = queue.popleft()
                for word2 in notVisited.copy():
                    if word1[1:] == word2[1:] or word1[:-1] == word2[:-1]:
                        if word2 == endWord:
                            return count
                        notVisited.discard(word2)
                        queue.append(word2)

                    for i in range(1, len(word1) - 1):
                        if word1[:i] == word2[:i] and word1[i+1:] == word2[i+1:]:
                            # It is a neighbor word
                            if word2 == endWord:
                                return count
                            notVisited.discard(word2)
                            queue.append(word2)
        return 0
