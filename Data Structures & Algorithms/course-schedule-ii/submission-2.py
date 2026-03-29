from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # We need to do a topological sort of the courses
        # If we find a loop return []
        # Let's first build the graph representing which courses the prerequisites for the course i
        parentOf = [set() for _ in range(numCourses)]
        childrenOf = [set() for _ in range(numCourses)]
        hasNoChildren = set(range(numCourses))
        for prerequisite in prerequisites:
            hasNoChildren.discard(prerequisite[1])
            parentOf[prerequisite[1]].add(prerequisite[0])
            childrenOf[prerequisite[0]].add(prerequisite[1])

        print(parentOf)
        print(childrenOf)
        # hasNoChildren are the leafs, which are guaranteed to have no parents
        queue = deque(hasNoChildren)
        print(queue)

        reversedResult = []
        # Now lets do a reversed BFS
        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()
                reversedResult.append(curr)
                print(curr, childrenOf[curr])
                for pre in childrenOf[curr]:
                    parentOf[pre].discard(curr)
                    if len(parentOf[pre]) == 0:
                        queue.append(pre)
            print(queue)
        return reversedResult[::-1] if len(reversedResult) == numCourses else []


        