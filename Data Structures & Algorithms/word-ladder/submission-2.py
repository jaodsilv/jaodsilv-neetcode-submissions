class Node:
    def __init__(self, word, reversed = False, index = 0):
        self.char = word[index]
        self.index = index
        if reversed:
            self.words = set([word[::-1]])
        else:
            self.words = set([word])
        self.next = None
        if index < len(word) - 1:
            self.next = {}
            child = Node(word, reversed, index + 1)
            self.next[word[index + 1]] = child

    def add(self, word, reversed = False, index = 0):
        if reversed:
            self.words.add(word[::-1])
        else:
            self.words.add(word)

        if index == len(word) - 1:
            return
        if word[index + 1] not in self.next:
            child = Node(word, reversed, index + 1)
            self.next[word[index + 1]] = child
        else:
            child = self.next[word[index + 1]]
            child.add(word, reversed, index + 1)        

class SufixPrefixTree:
    def __init__(self):
        self.prefixes = {}
        self.sufixes = {}

    def _innerAdd(self, word, group, reversed = False):
        if word[0] not in group:
            rootPrefix = Node(word, reversed)
            group[word[0]] = rootPrefix
        else:
            rootPrefix = group[word[0]]
            rootPrefix.add(word, reversed)

    def add(self, word):
        self._innerAdd(word, self.prefixes)
        self._innerAdd(word[::-1], self.sufixes, True)

    def _getWordIxes(self, word, group):
        print([n for n in group.keys()])
        node = group[word[0]]
        res = [node]
        for i in range(1, len(word)):
            c = word[i]
            node = node.next[c]
            res.append(node)
        return res
        
    def getPrefixes(self, word):
        return self._getWordIxes(word, self.prefixes)
    def getSufixes(self, word):
        return self._getWordIxes(word[::-1], self.sufixes)[::-1]

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: #O(len(wordlist))
            return 0
        if beginWord == endWord:
            return 1
        if len(beginWord) == 1:
            return 2


        '''
        Perhaps building a prefix tree
        And inserting all word there
        then backtrack all that have a single character and trying to go from there
        2 word have a single letter difference when there is a ramification of a node where, except for the letter of the bifurcation there is a path to the leaf where the characters are the same
        We could start top down, or bottom up
        '''
        tree = SufixPrefixTree()
        tree.add(beginWord)
        for word in wordList:
            tree.add(word)

        visited = set()
        DP = {}
        def dfs(word, noindex):
            print(word)
            if word == endWord:
                return 1

            minimum = len(wordList) + 1
            if word in visited:
                return minimum
            visited.add(word)
            prefixes = tree.getPrefixes(word)
            sufixes = tree.getSufixes(word)

            # Special cases for diff in the first and last characters

            for i in range(len(word)):
                if i == noindex:
                    continue
                words = set()
                if i == 0:
                    words = sufixes[1].words.copy()
                    print(0, sufixes[i].words)
                elif i == len(word) - 1:
                    print(len(word) - 1, prefixes[i - 1].words)
                    words = prefixes[i - 1].words.copy()
                else:
                    print(i, sufixes[i + 1].words)
                    print(i, prefixes[i - 1].words)
                    words = (prefixes[i - 1].words & sufixes[i + 1].words) - visited
                words.discard(word)
                print(words)
                for w in words:
                    total = dfs(w, i)
                    minimum = min(minimum, total)
            return minimum + 1


        dist = dfs(beginWord, -1)
        return 0 if dist > len(wordList) else dist
