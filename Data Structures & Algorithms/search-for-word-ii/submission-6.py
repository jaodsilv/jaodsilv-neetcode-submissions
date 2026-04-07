from collections import defaultdict
class Node:
    def __init__(self, word, i=0, prev=None) -> None:
        self.c = word[i]
        self.word = word if i == len(word) - 1 else None
        self.prev = prev
        self.next = {}
        if not self.word:
            self.next[word[i+1]] = Node(word, i+1, self)

    def add_word(self, word, i=1):
        if i == len(word):
            self.word = word
        elif word[i] in self.next:
            self.next[word[i]].add_word(word, i+1)
        else:
            self.next[word[i]] = Node(word, i, self)

    def find_word(self, word, i=1):
        if i == len(word) and self.word:
            return True
        return word[i] in self.next and self.next[word[i]].find_word(word, i+1)

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        nodes = {}
        for word in words:
            if word[0] in nodes:
                nodes[word[0]].add_word(word)
            else:
                nodes[word[0]] = Node(word)

        visited = set()
        res = set()
        def dfs(i, j, node):
            if node.word:
                res.add(node.word)
            visited.add((i, j))
            if i > 0 and (i-1, j) not in visited and board[i-1][j] in node.next:
                dfs(i-1, j, node.next[board[i-1][j]])
            if j > 0 and (i, j-1) not in visited and board[i][j-1] in node.next:
                dfs(i, j-1, node.next[board[i][j-1]])
            if i < len(board) - 1 and (i+1, j) not in visited and board[i+1][j] in node.next:
                dfs(i+1, j, node.next[board[i+1][j]])
            if j < len(board[0]) - 1 and (i, j+1) not in visited and board[i][j+1] in node.next:
                dfs(i, j+1, node.next[board[i][j+1]])
            visited.discard((i, j))

        for i, r in enumerate(board):
            for j, v in enumerate(r):
                if v in nodes:
                    dfs(i, j, nodes[v])
        return list(res)
