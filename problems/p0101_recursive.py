import unittest
from tree import TreeNode


def _symmetric(left, right):
    if not left or not right:
        return left is right
    return left.val == right.val and _symmetric(left.left, right.right) and _symmetric(left.right, right.left)


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return not root or _symmetric(root.left, root.right)


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 2, 3, 4, 4, 3], True)
        self._test([1, 2, 2, None, 3, None, 3], False)

    def _test(self, root, expected):
        root = TreeNode.from_array(root)
        actual = Solution().isSymmetric(root)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
