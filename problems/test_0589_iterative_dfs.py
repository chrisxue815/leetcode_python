from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


# O(n) time. O(depth) space. Iterative DFS.
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        result = []
        stack = [root]

        while stack:
            curr = stack.pop()
            result.append(curr.val)
            stack += reversed(curr.children)

        return result
