import bisect
class TreeNode:
    def __init__(self, word, i=0):
        self.next = {}
        # self.char = word[i]
        if i == len(word) - 1:
            self.word=True
        else:
            self.word=False
            self.next[word[i+1]] = TreeNode(word, i+1)
    def addWord(self, word, i=0):
        if i == len(word)-1:
            self.word=True
        elif word[i+1] in self.next:
            self.next[word[i+1]].addWord(word, i+1)
        else:
            self.next[word[i+1]] = TreeNode(word, i+1)

    def wordPrefix(self, word, i=0, minI=0):
        if self.word and i >= minI:
            return (self, i)
        if i >= len(word) - 1:
            return (None, 0)
        if word[i+1] not in self.next:
            return (None, 0)
        return self.next[word[i+1]].wordPrefix(word, i+1, minI)

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        DFS -> logn to get the next valid words, but we have to dig letter by letter.
        Perhaps using a prefix tree would work better
        '''
        # myDict = {}
        # for word in wordDict:
        #     if word[0] in myDict:
        #         myDict[word[0]].addWord(word)
        #     else:
        #         myDict[word[0]] = TreeNode(word)

        wordDict.sort()
        myDict = {word: i for i, word in enumerate(wordDict)}
        tested = set()
        def dfs(word: str):
            print(word)
            if len(word) == 0:
                return True
            if word in tested:
                return False
            tested.add(word)
            # This will return the index of the word that has the closest prefix, if any.
            # If there is a total match, it wil be in index, if not, we have to move backwards to find valid prefixes
            index = bisect.bisect_left(wordDict, word)
            if index < len(wordDict) and wordDict[index] == word:
                return True
            index -= 1
            while index >= 0 and word.startswith(wordDict[index]):
                if dfs(word[len(wordDict[index]):]):
                    return True
                index -= 1
            return False

        return dfs(s)
