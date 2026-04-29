from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # This is a topological sorting
        parentsCount = defaultdict(int)
        graph = defaultdict(list)
        hasNoParent = set(range(numCourses))
        for a, b in prerequisites:
            hasNoParent.discard(a)
            parentsCount[a] += 1
            graph[b].append(a)
        sorting = []
        while hasNoParent:
            sorting.append(hasNoParent.pop())
            for child in graph[sorting[-1]]:
                parentsCount[child] -= 1
                if parentsCount[child] == 0:
                    hasNoParent.add(child)
        if len(sorting) < numCourses:
            return []
        else:
            return sorting