import unittest
from tree import TreeNode


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


class Test(unittest.TestCase):
    def test_serialize(self):
        self._test([1, 1, 1, None, 1, 1, None, None, None, 1, None], 4)

    def _test(self, vals, expected):
        root = TreeNode.from_array(vals)
        actual = Solution().maxDepth(root)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
