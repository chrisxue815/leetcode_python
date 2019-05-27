import unittest
from tree import TreeNode


class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        sum_ = 0
        stack = []

        while root or stack:
            if root:
                if root.left and not root.left.left and not root.left.right:
                    sum_ += root.left.val
                    root = root.right
                else:
                    stack.append(root.right)
                    root = root.left
            else:
                root = stack.pop()

        return sum_


class Test(unittest.TestCase):
    def test(self):
        self._test([3, 9, 20, None, None, 15, 7], 24)

    def _test(self, vals, expected):
        root = TreeNode.from_array(vals)
        actual = Solution().sumOfLeftLeaves(root)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
