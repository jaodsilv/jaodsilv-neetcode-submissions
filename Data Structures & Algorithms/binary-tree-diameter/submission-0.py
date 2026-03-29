# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
        Let's store a few numbers:
        1. The current height from the root
        2. The current longest leg found
        3. The current length from longestLeg
        4. The current longest Length
        '''
        if root is None:
            return 0

        def longestLeg(root):
            longestPaths = []
            path = []
            h = 0
            longestLegH = 0
            stack = [(root, 0)]
            while stack:
                node, height = stack.pop()
                path.append(node)
                if node.right is not None:
                    stack.append((node.right, height + 1))
                if node.left is not None:
                    stack.append((node.left, height + 1))
                if node.right is None and node.left is None: # It is a leaf
                    if height > longestLegH:
                        longestLegH = height
                        longestPaths = [path[::-1]]
                    elif height == longestLegH:
                        longestPaths.append(path[::-1])
                    path.pop()
            return (longestLegH, longestPaths)

        # Now we travle from top to bottom to find the longest distance, which is the longest leg of the subtree
        legH, longestLegs = longestLeg(root)
        print(legH, longestLegs)
        maxDist = h = legH
        visited = set()

        # We are starting with a distance of longestLeg
        while longestLegs:
            leg = longestLegs.pop()
            currDist = legH + 1
            
            while leg[-1] in visited:
                leg.pop()
                currDist -= 1

            visited.add(leg[-1])

            while leg:
                node = leg.pop()
                currDist -= 1
                if 2 * currDist <= maxDist:
                    break

                if node.right is None or node.left is None: # It does not beyond currDist
                    continue

                print("currDist", currDist)
                if node.right == leg[-1]:
                    root = node.left
                else:
                    root = node.right
                h, _ = longestLeg(root)
                maxDist = max(maxDist, h + currDist + 1)
        return maxDist
