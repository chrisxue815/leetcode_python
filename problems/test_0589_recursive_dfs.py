from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


# O(n) time. O(depth) space. Recursive DFS.
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        result = []

        def dfs(curr):
            result.append(curr.val)

            for child in curr.children:
                dfs(child)

        dfs(root)
        return result
