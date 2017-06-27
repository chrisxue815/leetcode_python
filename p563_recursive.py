import unittest
from tree import TreeNode


def _sum_and_tilt_sum(root):
    if not root:
        return 0, 0
    left_sum, left_tilt = _sum_and_tilt_sum(root.left)
    right_sum, right_tilt = _sum_and_tilt_sum(root.right)
    return left_sum + right_sum + root.val, left_tilt + right_tilt + abs(left_sum - right_sum)


class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return _sum_and_tilt_sum(root)[1]


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 3], 1)

    def _test(self, vals, expected):
        root = TreeNode.from_array(vals)
        actual = Solution().findTilt(root)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
