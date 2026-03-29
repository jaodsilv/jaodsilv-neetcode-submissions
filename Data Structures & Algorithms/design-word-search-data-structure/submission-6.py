class Node:
    def __init__(self, index, word):
        self.index = index
        self.val = word[index]
        self.word = index == len(word) - 1
        self.next = {}

class WordDictionary:
    def __init__(self):
        self.words = set()
        self.prefixTree = {} # Up to 26 nodes in the current level

    def addWord(self, word: str) -> None:
        if word in self.words:
            return
        node = None
        
        if word[0] not in self.prefixTree:
            node = Node(0, word)
            self.prefixTree[word[0]] = node
        else:
            node = self.prefixTree[word[0]]

        for i in range(1, len(word)):
            prev = node
            if word[i] in prev.next:
                node = prev.next[word[i]]
            else:
                node = Node(i, word)
                prev.next[word[i]] = node

        node.word = True

    def search(self, word: str) -> bool:
        if word in self.words:
            return True
        print(self.prefixTree)
        stack = [(self.prefixTree, 0)]
        while stack:
            nodes, i = stack.pop()
            c = word[i]
            print(word[i])
            if c == '.':
                for v in nodes.values():
                    if i == len(word) - 1:
                        if v.word:
                            return True
                    else:
                        stack.append((v.next, i + 1))
            elif c in nodes:
                if i == len(word) - 1:
                    if nodes[c].word:
                        return True
                else:
                    stack.append((nodes[c].next, i + 1))
        return False
