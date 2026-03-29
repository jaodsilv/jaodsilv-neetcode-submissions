class Node:
    def __init__(self, word, i=0):
        self.next = {}
        self.i = i
        self.c = word[i]
        if i == len(word) - 1:
            self.word = True
        else:
            self.word = False
            self.next[word[i+1]] = Node(word, i+1)

    def insert(self, word, i=0):
        if i == len(word) - 1:
            self.word = True
        elif word[i+1] in self.next:
            self.next[word[i+1]].insert(word, i+1)
        else:
            self.next[word[i+1]] = Node(word, i+1)

class PrefixTree:
    def __init__(self):
        self.words = {}

    def insert(self, word: str) -> None:
        if word[0] in self.words:
            self.words[word[0]].insert(word)
        else:
            self.words[word[0]] = Node(word)



    def search(self, word: str) -> bool:
        words = self.words
        node = None
        for c in word:
            if c in words:
                node = words[c]
                words = node.next
            else:
                return False
        return node is not None and node.word

    def startsWith(self, prefix: str) -> bool:
        words = self.words
        node = None
        for c in prefix:
            if c in words:
                node = words[c]
                words = node.next
            else:
                return False
        return True
        