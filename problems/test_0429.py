class Node(object):
    """
    # Definition for a Node.
    """

    def __init__(self, val, children):
        self.val = val
        self.children = children


# O(n) time. O(max number of nodes on the same level) space. BFS.
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []

        result = []
        q = [root]

        while q:
            level = []
            new_q = []

            for node in q:
                level.append(node.val)
                new_q += node.children

            result.append(level)
            q = new_q

        return result
