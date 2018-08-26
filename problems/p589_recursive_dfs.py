class Node(object):
    """
    # Definition for a Node.
    """

    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        result = []

        def dfs(curr):
            if not curr:
                return

            result.append(curr.val)

            for child in curr.children:
                dfs(child)

        dfs(root)
        return result
