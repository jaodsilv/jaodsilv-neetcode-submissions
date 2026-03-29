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

    def wordPrefix(self, word, i=0):
        if self.word:
            return (self, i)
        if i >= len(word) - 1:
            return (None, 0)
        if word[i+1] not in self.next:
            return (None, 0)
        return self.next[word[i+1]].wordPrefix(word, i+1)

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        myDict = {}
        for word in wordDict:
            if word[0] in myDict:
                myDict[word[0]].addWord(word)
            else:
                myDict[word[0]] = TreeNode(word)

        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        
        t = max([len(w) for w in wordDict])

        for i in range(len(s)-1, -1, -1):
            if s[i] not in myDict:
                continue
            node = myDict[s[i]]
            j = i
            while node and j < min(len(s), i + t):
                if node.word and dp[j+1]:
                    dp[i] = True
                if j < len(s)-1:
                    if s[j+1] not in node.next:
                        break
                    else:
                        node = node.next[s[j+1]]
                j+=1
        print(dp)
        return dp[0]
