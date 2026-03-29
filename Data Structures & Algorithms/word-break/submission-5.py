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

        myDict = set(wordDict)
        tested = set()
        def dfs(i):
            print(i)
            if i == len(s):
                return True
            if i in tested:
                return False
            tested.add(i)
            j = i + 1
            while j <= len(s):
                if s[i:j] in myDict:
                    res = dfs(j)
                    if res:
                        return True
                j += 1
            return False

        return dfs(0)
