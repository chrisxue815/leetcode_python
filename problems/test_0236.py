import unittest
from tree import TreeNode, null


class Solution:
    def __init__(self):
        self.p = None
        self.q = None
        self.lca = None

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.p = p
        self.q = q
        self._num_matches(root)
        return self.lca

    def _num_matches(self, root):
        if not root:
            return 0

        num_left_matches = self._num_matches(root.left)
        if num_left_matches == 2:
            return 2

        if root is self.p or root is self.q:
            num_left_matches += 1
        if num_left_matches == 2:
            self.lca = root
            return 2

        num_right_matches = self._num_matches(root.right)
        if num_left_matches == 1 and num_right_matches == 1:
            self.lca = root
            return 2

        return num_left_matches + num_right_matches


class Test(unittest.TestCase):
    def test(self):
        root = TreeNode.from_array([3, 5, 1, 6, 2, 0, 8, null, null, 7, 4])
        self._test(root, root.left, root.right, root)
        self._test(root, root.left, root.left.right.right, root.left)
        self._test(root, root.right.left, root.right.right, root.right)
        self._test(root, root.left, TreeNode(0), None)

    def _test(self, root, p, q, expected):
        actual = Solution().lowestCommonAncestor(root, p, q)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
