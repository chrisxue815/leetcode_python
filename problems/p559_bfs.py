class Node(object):
    """
    # Definition for a Node.
    """

    def __init__(self, val, children):
        self.val = val
        self.children = children


# O(V) time. O(max number of nodes on the same level) space. BFS.
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0

        depth = 0
        q = [root]

        while q:
            new_q = []

            for curr in q:
                new_q += curr.children

            depth += 1
            q = new_q

        return depth
