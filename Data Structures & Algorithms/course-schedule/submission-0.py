class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # This is about detecting cycles in a directed graph. If there is any, then return False
        # Let's find who does not have a parent, i.e., which courses are roots
        roots = set(range(numCourses))
        # Let's create a map of relationships, parent to all children
        children = []
        parents = []
        for i in range(numCourses):
            children.append(set())
            parents.append(set())
        for relationship in prerequisites:
            roots.discard(relationship[1])
            children[relationship[0]].add(relationship[1])
            parents[relationship[1]].add(relationship[0])

        while roots:
            # Now let's dfs from each root if there is a loop somewhere
            # The graph is directional, so there might be a node which have to other nodes pointing to it.
            nextRoots = set()
            while roots:
                root = roots.pop()
                for candidate in children[root]:
                    parents[candidate].discard(root)
                    if len(parents[candidate]) == 0:
                        nextRoots.add(candidate)
                children[root].clear()
            roots = nextRoots

        for i in range(numCourses):
            if len(children[i]) > 0:
                return False
        return True

        '''
        A->B->C
        A->C
        Same root, two valid paths, but no loop

        VS

        A->B->C->D->B

        What if I go eliminating the roots, the selecting the new roots
        eg:
        A->B->C->D
        A->C->D
        E->D
        A->F->G->H->F

        First I eliminate A and E
        then we have only:
        B->C->D
        F->G->H->F
        and so on, at the end we will have 

        '''