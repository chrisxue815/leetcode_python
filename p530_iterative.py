import unittest
from tree import TreeNode


class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        min_diff = 0x7FFFFFFF
        prev = None
        stack = []

        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()

                if prev is not None:
                    min_diff = min(min_diff, root.val - prev)
                prev = root.val

                root = root.right

        return min_diff


class Test(unittest.TestCase):
    def test(self):
        self._test([1, None, 3, 2], 1)

    def _test(self, vals, expected):
        root = TreeNode.from_array(vals)
        actual = Solution().getMinimumDifference(root)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
