class Node:
    """
    # Definition for a Node.
    """

    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        result = []

        def dfs(curr):
            if not curr:
                return

            for child in curr.children:
                dfs(child)

            result.append(curr.val)

        dfs(root)
        return result
