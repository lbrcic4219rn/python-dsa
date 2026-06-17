from typing import Optional

from Graphs.Node import Node


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        copies = {}

        def dfs(node):
            if node in copies:
                return copies[node]

            copy = Node(node.val)
            copies[node] = copy

            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node) if not node else []
