class Node:
    def __init__(self, name, email) -> None:
        self.neighbors = []
        self.name = name
        self.email = email

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        nodes = {}
        for acc in accounts:
            name = acc[0]
            rootemail = acc[1]
            node = None
            if rootemail in nodes:
                node = nodes[rootemail]
            else:
                node = Node(name, rootemail)
                nodes[rootemail] = node
            
            for email in acc[2:]:
                nei = None
                if email in nodes:
                    nei = nodes[email]
                else:
                    nei = Node(name, email)
                    nodes[email] = nei
                nei.neighbors.append(node)
                node.neighbors.append(nei)

        # Now we find the connected components of this graph
        def dfs(node: Node) -> set:
            res = set([node.email])
            while node.neighbors:
                nei = node.neighbors.pop()
                if nei.email in nodes:
                    del nodes[nei.email]
                    res |= dfs(nei)
            return res
        res = []
        while nodes:
            email, node = nodes.popitem()
            name = node.name
            emails = dfs(node)
            res.append([name] + sorted(emails))
        return res
