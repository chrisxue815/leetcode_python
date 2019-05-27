import unittest
from tree import TreeNode


# O(n). Recursion.
class Solution:
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if not root:
            return None
        if root.val < L:
            return self.trimBST(root.right, L, R)
        elif root.val > R:
            return self.trimBST(root.left, L, R)
        else:
            root.left = self.trimBST(root.left, L, R)
            root.right = self.trimBST(root.right, L, R)
            return root


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 0, 2], 1, 2, [1, None, 2])
        self._test([3, 0, 4, None, 2, None, None, 1], 1, 3, [3, 2, None, 1])

    def _test(self, root, L, R, expected):
        root = TreeNode.from_array(root)
        actual = Solution().trimBST(root, L, R)
        actual = actual.to_array()
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
