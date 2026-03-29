class TreeNode:
    def __init__(self, word, i=0):
        self.next = {}
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
        myDict = {}
        for word in wordDict:
            if word[0] in myDict:
                myDict[word[0]].addWord(word)
            else:
                myDict[word[0]] = TreeNode(word)

        print(myDict)
        tested = set()
        def dfs(i):
            if i == len(s):
                return True
            if i in tested:
                return False
            if s[i] not in myDict:
                tested.add(i)
                return False
            tested.add(i)
            j = i
            node = myDict[s[i]]
            minI = i
            while True:
                node, j = node.wordPrefix(s, j, minI)
                if node is None:
                    return False
                res = dfs(j+1)
                minI = j+1
                if res:
                    return True              

        return dfs(0)
