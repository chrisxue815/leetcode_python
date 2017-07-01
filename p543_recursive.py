import unittest
from tree import TreeNode


def _height_and_diameter(root):
    if not root:
        return 0, 0
    lh, ld = _height_and_diameter(root.left)
    rh, rd = _height_and_diameter(root.right)
    return max(lh, rh) + 1, max(ld, rd, lh + rh)


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return _height_and_diameter(root)[1]


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 3, 4, 5], 3)

    def _test(self, root, expected):
        root = TreeNode.from_array(root)
        actual = Solution().diameterOfBinaryTree(root)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
