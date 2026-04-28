class WordDictionary:
    def __init__(self):
        self.dict = {}

    def addWord(self, word: str) -> None:
        node = self.dict
        for c in word:
            if c in node:
                node = node[c]
            else:
                node[c] = {}
                node = node[c]
        node['word'] = {}


    def _search(self, word: str, node) -> bool:
        if len(word) == 0:
            return 'word' in node
        for i, c in enumerate(word):
            if c != '.':
                if c not in node:
                    return False
                node = node[c]
            else:
                for node in node.values():
                    if self._search(word[i+1:], node):
                        return True
                return False
        return 'word' in node

    def search(self, word: str) -> bool:
        node = self.dict
        for i, c in enumerate(word):
            if c != '.':
                if c not in node:
                    return False
                node = node[c]
            else:
                for node in node.values():
                    if self._search(word[i+1:], node):
                        return True
                return False
        return 'word' in node

