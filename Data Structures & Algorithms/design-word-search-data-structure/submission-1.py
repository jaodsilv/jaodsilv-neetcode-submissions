# Using a trie
class Node:
    def __init__(self, suffix):
        self.children = [None] * 26
        if len(suffix) == 0:
            self.isWord = True
        else:
            self.children[ord(suffix[0]) - ord('a')] = Node(suffix[1:])
            self.isWord = False

    def addSuffix(self, suffix):
        if len(suffix) == 0:
            self.isWord = True
        elif not self.children[ord(suffix[0]) - ord('a')]:
            self.children[ord(suffix[0]) - ord('a')] = Node(suffix[1:])
        else:
            self.children[ord(suffix[0]) - ord('a')].addSuffix(suffix[1:])

    def search(self, suffix):
        if len(suffix) == 0:
            return self.isWord
        if suffix[0] == '.':
            for child in self.children:
                if child and child.search(suffix[1:]):
                    return True
            return False
        elif not self.children[ord(suffix[0]) - ord('a')]:
            return False
        else:
            return self.children[ord(suffix[0]) - ord('a')].search(suffix[1:])



class WordDictionary:
    def __init__(self):
        self.words = [None] * 26

    def addWord(self, word: str) -> None:
        if len(word) > 0:
            if self.words[ord(word[0]) - ord('a')]:
                self.words[ord(word[0]) - ord('a')].addSuffix(word[1:])
            else:
                self.words[ord(word[0]) - ord('a')] = Node(word[1:])

    def search(self, word: str) -> bool:
        if word == '.':
            for i in self.words:
                if i and i.isWord:
                    return True
            return False
        if word[0] == '.':
            for node in self.words:
                if node and node.search(word[1:]):
                    return True
            return False
        elif not self.words[ord(word[0]) - ord('a')]:
            return False
        else:
            return self.words[ord(word[0]) - ord('a')].search(word[1:])