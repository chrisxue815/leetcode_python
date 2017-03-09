import unittest
from tree import TreeNode, null


class Solution(object):
    def __init__(self):
        self.max = None

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        self._max_path_sum(root)
        return self.max

    def _max_path_sum(self, root):
        if root.left:
            leftmax = self._max_path_sum(root.left)
        else:
            leftmax = 0

        if root.right:
            rightmax = self._max_path_sum(root.right)
        else:
            rightmax = 0

        max_sum_as_root = max(root.val, root.val + leftmax, root.val + rightmax)
        max_sum_containing_root = max(max_sum_as_root, root.val + leftmax + rightmax)

        if not self.max or max_sum_containing_root > self.max:
            self.max = max_sum_containing_root

        return max_sum_as_root


class Test(unittest.TestCase):
    def test_serialize(self):
        self._test([1, 2, 3], 6)
        self._test([5, 4, 8, 11, null, 13, 4, 7, 2, null, null, null, 1], 48)

    def _test(self, vals, expected):
        root = TreeNode.from_array(vals)
        self.assertEqual(Solution().maxPathSum(root), expected)


if __name__ == '__main__':
    unittest.main()
