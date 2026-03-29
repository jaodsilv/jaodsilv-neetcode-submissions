import heapq

MAX_DIST = 4000001

class Node:
    def __init__(self, point, index):
        self.x = point[0]
        self.y = point[1]
        self.index = index
        self.__parent = self
        self.size = 1

    def dist(self, nei: 'Node') -> int:
        return abs(self.x - nei.x) + abs(self.y - nei.y)

    @property
    def parent(self):
        if self == self.__parent:
            return self
        self.__parent = self.__parent.parent
        return self.__parent

    @parent.setter
    def parent(self, other: 'Node'):
        self.__parent = other

    def merge(self, other: 'Node', parents: Set['Node']):
        parent1 = self.parent 
        parent2 = other.parent
        parent = parent1
        if parent1.size > parent2.size:
            parent2.parent = parent1
            parent1.size += parent2.size
            parents.discard(parent2)
            parents.add(parent1)
        else:
            parent1.parent = parent2
            parent2.size += parent1.size
            parents.add(parent2)
            parents.discard(parent1)
            parent = parent2
        return parent

    def __lt__(self, value) -> bool:
        return self.index < value.index

    def __eq__(self, value: object, /) -> bool:
        if not value:
            return False
        if isinstance(value, int):
            return self.index == value
        return type(self) == type(value) and self.index == value.index

    def __ne__(self, value: object, /) -> bool:
        return not self.__eq__(value)

    def __hash__(self):
        return hash(self.index)

    def __repr__(self):
        return self.__str__()
    def __str__(self):
        return f'({self.x}, {self.y})'

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 0

        # Create Nodes
        nodes = []
        for i, p in enumerate(points):
            nodes.append(Node(p, i))
        
        # Process Nodes one by one, finding the minimum Distance Node
        total = 0
        heap = [(0, nodes[0])]
        notConnected = set(nodes)


        while heap:
            cost, node = heapq.heappop(heap)
            total += cost
            notConnected.discard(node)
            for m in notConnected:
                heapq.heappush(heap, (node.dist(m), m))
            while heap and heap[0][1] not in notConnected:
                heapq.heappop(heap)
        return total



