class Node(object):
    """
    # Definition for a Node.
    """

    def __init__(self, val, children):
        self.val = val
        self.children = children


# O(V) time. O(depth) space. Recursive DFS.
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0

        return 1 + max(self.maxDepth(child) for child in root.children) if root.children else 1
