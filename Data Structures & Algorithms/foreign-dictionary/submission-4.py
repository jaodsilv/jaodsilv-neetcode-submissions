class Node:
    def __init__(self, char):
        self.char = char
        self.depth = -1
        self.children = set()

    def add(self, child):
        self.children.add(child)


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        '''
        Solution idea 1:
        We can think of the words as in a prefix tree.
        Each level to be added in the lexicography order
        Then we travel the prefix tree learn the order

        Solution idea 2:
        We go traveling the letters by level.
        When first letter is the same, we go to the next one of those words
        Then we know for sure where they fit
        e.g.
        ["hrn","hrf","er","enn","rfnn"]
        word 0 and 1:
        h is the same
        r is the same
        n < f

        word 1 and 2
        h < e

        word 2 and 3
        e is the same
        r < n

        words 3 and 4
        e < r

        then we know h < e < r < n < f
        '''

        if len(words) == 1 and len(words[0]) == 1:
            return words[0]

        if len(words) <= 1:
            return ""

        # let's build that information as a graph
        # As a graph it must have a path in which all nodes can be visited and there must exist NO cycles
        # This is equivalent to say that there is path in which ALL child nodes are not visited yet
        nodes = {}
        isChild = set()
        isParent = set()
        alphaSet = set()
        for i in range(len(words) - 1):
            wordLeft = words[i]
            wordRight = words[i + 1]
            count = 0
            for l, r in zip(wordLeft, wordRight):
                count += 1
                # print(l, r)
                if l not in nodes:
                    alphaSet.add(l)
                    nodes[l] = Node(l)
                if l != r:
                    if r not in nodes:
                        alphaSet.add(r)
                        nodes[r] = Node(r)
                    nodes[l].add(nodes[r])
                    isChild.add(r)
                    isParent.add(l)
                    break
            
            if count == len(wordRight) and wordRight == wordLeft[:len(wordRight)] and count < len(wordLeft):
                return ""
            for j in range(count, len(wordLeft)):
                #print(wordLeft[j])
                if wordLeft[j] not in nodes:
                    alphaSet.add(wordLeft[j])
                    nodes[wordLeft[j]] = Node(wordLeft[j])
            for j in range(count, len(wordRight)):
                #print(wordRight[j])
                if wordRight[j] not in nodes:
                    alphaSet.add(wordRight[j])
                    nodes[wordRight[j]] = Node(wordRight[j])

        start = alphaSet - isChild
        perLevel = []

        # Good for loop detection
        visited = set()

        def visit(node, level):
            print('Visiting', node.char)
            if node.char in visited:
                print('False on', node.char)
                return False

            visited.add(node.char)
            if level <= node.depth:
                return True

            if node.depth >= 0:
                perLevel[node.depth].discard(node.char)
            if len(perLevel) == level:
                perLevel.append(set())
            perLevel[level].add(node.char)

            node.depth = level

            for child in node.children:
                if not visit(child, level + 1):
                    print(False)
                    return False

            visited.discard(node.char)
            return True

        # If there is more than one valid path, then we have to find all of them
        for rootChar in start:
            #print('Starting', rootChar)
            visited = set()
            if not visit(nodes[rootChar], 0):
                print(False)
                return ""
        
        res = ""
        for level in perLevel:
            for char in level:
                res = res + char
        if len(res) < len(alphaSet):
            return ""
        return res