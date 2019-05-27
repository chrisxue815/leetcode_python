class Node:
    """
    # Definition for a QuadTree node.
    """

    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


# O(n^2) time. O(n) space. Recursion.
class Solution:
    def intersect(self, a, b):
        """
        :type a: Node
        :type b: Node
        :rtype: Node
        """
        if a.isLeaf:
            return a if a.val else b
        if b.isLeaf:
            return b if b.val else a

        tl = self.intersect(a.topLeft, b.topLeft)
        tr = self.intersect(a.topRight, b.topRight)
        bl = self.intersect(a.bottomLeft, b.bottomLeft)
        br = self.intersect(a.bottomRight, b.bottomRight)

        if tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf and tl.val == tr.val == bl.val == br.val:
            return tl
        else:
            return Node(False, False, tl, tr, bl, br)
