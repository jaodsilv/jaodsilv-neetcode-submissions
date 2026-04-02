from collections import deque
class Node:
    def __init__(self, word, i = 0) -> None:
        self.val = word[i]
        self.word = i == len(word) - 1
        self.next = {} if self.word else {word[i+1]: Node(word, i+1)}

    def add_word(self, word, i = 1) -> None:
        if i == len(word):
            self.word = True
        elif word[i] in self.next:
            self.next[word[i]].add_word(word, i+1)
        else:
            self.next[word[i]] = Node(word, i)

    def find(self, word, i = 1) -> bool:
        if i == len(word):
            return self.word
        return word[i] in self.next and self.next[word[i]].find(word, i+1)

        
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = {}
        for word in wordDict:
            if word[0] in words:
                words[word[0]].add_word(word)
            else:
                words[word[0]] = Node(word)
        
        queue = deque([0])
        tested = set()
        while queue:
            i = queue.popleft()
            if i in tested or s[i] not in words:
                continue
            tested.add(i)
            node = words[s[i]]
            j = i + 1
            if node.word:
                queue.append(j)
            while j < len(s) and s[j] in node.next:
                node = node.next[s[j]]
                if node.word:
                    queue.append(j + 1)
                j += 1
            if queue and queue[-1] == len(s):
                return True
        return False