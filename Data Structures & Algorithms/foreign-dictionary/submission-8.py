class Node:
    def __init__(self, value):
        self.value = value
        self.next = set()
        self.prev = set()

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        if len(words) == 1:
            return "".join(set(words[0]))

        # Let's first build a graph of the orders
        chars = {}
        # O(m*n)
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            j = 0
            while j < min(len(word1), len(word2)) and word1[j] == word2[j]:
                if word1[j] not in chars:
                    chars[word1[j]] = Node(word1[j])
                j += 1

            if j < min(len(word1), len(word2)):
                if word1[j] not in chars:
                    chars[word1[j]] = Node(word1[j])
                if word2[j] not in chars:
                    chars[word2[j]] = Node(word2[j])

                node1 = chars[word1[j]]
                node2 = chars[word2[j]]
                node1.next.add(word2[j])
                node2.prev.add(word1[j])
            elif len(word1) > len(word2):
                return ""
            for k in range(j + 1, max(len(word1), len(word2))):
                if k < len(word1) and word1[k] not in chars:
                    chars[word1[k]] = Node(word1[k])
                if k < len(word2) and word2[k] not in chars:
                    chars[word2[k]] = Node(word2[k])

        noParents = set()
        # nochildren = set()
        # added = set()
        res = []
        # Capture independent nodes which order is irrelevant and initial set of noChildren and noParents values
        for char, node in chars.items():
            # if not node.next and not node.prev:
            #     res.append(node.value)
            #     added.add(node.value)
            #     del chars[node.value]
            # el
            # if not node.next:
            #     noChildren.add(node)
            # el
            if not node.prev:
                noParents.add(char)

        while noParents:
            for char in noParents.copy():
                node = chars[char]
                for next in node.next:
                    nextNode = chars[next]
                    nextNode.prev.remove(char)
                    if not nextNode.prev:
                        noParents.add(next)
                noParents.remove(char)
                del chars[char]
                # if char in added:
                #     return ""
                # added.add(char)
                res.append(char)
        if chars:
            # Meaning there is a loop
            return ""
        return "".join(res)