import unittest
from tree import TreeNode


class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)


class Test(unittest.TestCase):
    def test(self):
        self._test([3, 9, 20, None, None, 15, 7], 24)

    def _test(self, vals, expected):
        root = TreeNode.from_array(vals)
        actual = Solution().sumOfLeftLeaves(root)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
