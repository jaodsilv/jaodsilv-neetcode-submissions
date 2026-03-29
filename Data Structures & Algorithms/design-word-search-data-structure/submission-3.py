# This word dictionery should suport wild cards
# Let's create a prefix tree with wildcards
class DictNode:
    def __init__(self, word, i, isWild = False):
        if isWild:
            self.char = '.'
        else:
            self.char = word[i]
        self.children = {}
        if i == len(word) - 1:
            self.isWord = True
        else:
            self.isWord = False
            self.children['.'] = DictNode(word, i+1, isWild=True)
            self.children[word[i+1]] = DictNode(word, i+1)
        
    def addWord(self, word, i):
        if i == len(word) - 1:
            self.isWord = True
        else:
            if word[i+1] in self.children:
                self.children[word[i+1]].addWord(word, i+1)
            else:
                self.children[word[i+1]] = DictNode(word, i+1)

            if '.' in self.children:
                self.children['.'].addWord(word, i+1)
            else:
                self.children['.'] = DictNode(word, i+1, isWild=True)

    def search(self, word, i):
        if i == len(word) - 1:
            return self.isWord
        return word[i+1] in self.children and self.children[word[i + 1]].search(word, i + 1)

class WordDictionary:
    def __init__(self):
        self.words = {}

    def addWord(self, word: str) -> None:
        if word[0] in self.words:
            self.words[word[0]].addWord(word, 0)
        else:
            self.words[word[0]] = DictNode(word, 0)

        if '.' in self.words:
            self.words['.'].addWord(word, 0)
        else:
            self.words['.'] = DictNode(word, 0, isWild=True)
        

    def search(self, word: str) -> bool:
        return word[0] in self.words and self.words[word[0]].search(word, 0)
