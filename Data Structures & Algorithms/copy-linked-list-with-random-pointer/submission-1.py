"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        node = head
        nodesList = [node]
        i = 1
        valsMap = {node.val: [0]}
        copyHead = Node(node.val)
        copy = copyHead
        nodes = [copy]
        while node.next:
            node = node.next
            copy.next = Node(node.val)
            copy = copy.next
            nodesList.append(node)
            nodes.append(copy)
            if node.val in valsMap:
                valsMap[node.val].append(i)
            else:
                valsMap[node.val] = [i]
            i += 1
        
        node = head
        copy = copyHead
        while node:
            if node.random:
                randomVal = node.random.val
                for i in valsMap[randomVal]:
                    if node.random == nodesList[i]:
                        copy.random = nodes[i]
            node = node.next
            copy = copy.next



        return copyHead
