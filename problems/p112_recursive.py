import unittest
from tree import TreeNode


def _has_sum(root, sum):
    return not root.left and not root.right and root.val == sum \
           or root.left and _has_sum(root.left, sum - root.val) \
           or root.right and _has_sum(root.right, sum - root.val)


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        return bool(root and _has_sum(root, sum))


class Test(unittest.TestCase):
    def test_serialize(self):
        self._test([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 22, True)
        self._test([], 0, False)

    def _test(self, root, sum, expected):
        root = TreeNode.from_array(root)
        actual = Solution().hasPathSum(root, sum)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
