# This word dictionery should suport wild cards
class DictNode:
    def __init__(self, word, i):
        self.char = word[i]
        self.sufixes = {}
        if i == len(word) - 1:
            self.isWord = True
        else:
            self.isWord = False
            self.sufixes[word[i+1]] = DictNode(word, i+1)
        
    def addWord(self, word, i):
        if i == len(word) - 1:
            self.isWord = True
        elif word[i+1] in self.sufixes:
            self.sufixes[word[i+1]].addWord(word, i+1)
        else:
            self.sufixes[word[i+1]] = DictNode(word, i+1)

    def search(self, word, i):
        if i >= len(word) - 1:
            return self.isWord
        if word[i+1] == '.':
            for v in self.sufixes.values(): 
                if v.search(word, i + 1):
                    return True
            return False
        else:
            return word[i+1] in self.sufixes and self.sufixes[word[i + 1]].search(word, i + 1)

class WordDictionary:
    def __init__(self):
        self.words = {}

    def addWord(self, word: str) -> None:
        if word[0] in self.words:
            self.words[word[0]].addWord(word, 0)
        else:
            self.words[word[0]] = DictNode(word, 0)

    def search(self, word: str) -> bool:
        if word[0] == '.':
            for _, v in self.words.items(): 
                if v.search(word, 0):
                    return True
            return False
        else:
            return word[0] in self.words and self.words[word[0]].search(word, 0)
