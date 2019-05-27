class Node:
    """
    # Definition for a Node.
    """

    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []

        result = []
        stack = [root]

        while stack:
            curr = stack.pop()
            result.append(curr.val)
            stack += reversed(curr.children)

        return result
