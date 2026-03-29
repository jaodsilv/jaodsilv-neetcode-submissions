class Node:
    def __init__(self, isWord = False):
        self.isWord = isWord
        self.children = [None] * 26

class PrefixTree:

    def __init__(self):
        self.root = [None] * 26

    def insert(self, word: str) -> None:
        if len(word) == 1:
            if not self.root[ord(word[0]) - ord('a')]:
                self.root[ord(word[0]) - ord('a')] = Node(isWord=True)
            else:
                self.root[ord(word[0]) - ord('a')].isWord = True
            return
        if not self.root[ord(word[0]) - ord('a')]:
            node = Node()
            self.root[ord(word[0]) - ord('a')] = node
        node = self.root[ord(word[0]) - ord('a')]
        for i in range(1, len(word)):
            next = node.children[ord(word[i]) - ord('a')]
            if not next:
                next = Node()
                node.children[ord(word[i]) - ord('a')] = next
            node = next
        node.isWord = True

    def search(self, word: str) -> bool:
        node = self.root[ord(word[0]) - ord('a')]
        if not node:
            return False
        for i in range(1, len(word)):
            if not node.children[ord(word[i]) - ord('a')]:
                return False
            node = node.children[ord(word[i]) - ord('a')]
        return node.isWord

    def startsWith(self, prefix: str) -> bool:
        node = self.root[ord(prefix[0]) - ord('a')]
        if not node:
            return False
        for i in range(1, len(prefix)):
            if not node.children[ord(prefix[i]) - ord('a')]:
                return False
            node = node.children[ord(prefix[i]) - ord('a')]
        return True