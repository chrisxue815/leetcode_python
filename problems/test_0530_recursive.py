import unittest
from tree import TreeNode


class Solution(object):
    def __init__(self):
        self.min_diff = 0x7FFFFFFF
        self.prev = None

    def _traverse(self, root):
        if not root:
            return
        self._traverse(root.left)

        if self.prev is not None:
            self.min_diff = min(self.min_diff, root.val - self.prev)
        self.prev = root.val

        self._traverse(root.right)

    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self._traverse(root)
        return self.min_diff


class Test(unittest.TestCase):
    def test(self):
        self._test([1, None, 3, 2], 1)

    def _test(self, vals, expected):
        root = TreeNode.from_array(vals)
        actual = Solution().getMinimumDifference(root)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
