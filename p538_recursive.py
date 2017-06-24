import unittest
from tree import TreeNode


class Solution(object):
    def __init__(self):
        self.sum_ = 0

    def _make_bst_greater_again(self, root):
        if not root:
            return 0

        self._make_bst_greater_again(root.right)

        self.sum_ += root.val
        root.val = self.sum_

        self._make_bst_greater_again(root.left)

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self._make_bst_greater_again(root)
        return root


class Test(unittest.TestCase):
    def test_serialize(self):
        self._test([5, 2, 13], [18, 20, 13])

    def _test(self, vals, expected):
        root = TreeNode.from_array(vals)
        actual = Solution().convertBST(root)
        actual = actual.to_array()
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
