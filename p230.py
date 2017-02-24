import unittest
from tree import TreeNode, null


class Solution(object):

    def __init__(self):
        self.k = 0
        self.kth = 0
        self.index = 0

    # optimize: self-balancing
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.k = k
        self._kth(root)
        return self.kth

    def _kth(self, node):
        if node is None:
            return False

        if self._kth(node.left):
            return True

        self.index += 1
        if self.index == self.k:
            self.kth = node.val
            return True

        if self._kth(node.right):
            return False


class Test(unittest.TestCase):

    def test(self):
        root = TreeNode.from_array([4, 2, 6, 1, 3, 5, 7])
        self.assertEqual(
            Solution().kthSmallest(root, 6),
            6)


if __name__ == '__main__':
    unittest.main()
