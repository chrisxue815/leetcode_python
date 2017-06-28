import unittest
from tree import TreeNode


class Solution(object):
    def __init__(self):
        self.sum_left_leaves = 0

    def _traverse(self, root):
        if not root:
            return

        if root.left:
            if root.left.left or root.left.right:
                self._traverse(root.left)
            else:
                self.sum_left_leaves += root.left.val

        self._traverse(root.right)

    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self._traverse(root)
        return self.sum_left_leaves


class Test(unittest.TestCase):
    def test(self):
        self._test([3, 9, 20, None, None, 15, 7], 24)

    def _test(self, vals, expected):
        root = TreeNode.from_array(vals)
        actual = Solution().sumOfLeftLeaves(root)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
