import unittest
from tree import TreeNode


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        stack = []
        curr = root

        while curr or stack:
            if curr:
                curr.left, curr.right = curr.right, curr.left
                stack.append(curr.right)
                curr = curr.left
            else:
                curr = stack.pop()

        return root


class Test(unittest.TestCase):
    def test_serialize(self):
        self._test([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1])

    def _test(self, vals, expected):
        root = TreeNode.from_array(vals)
        actual = Solution().invertTree(root)
        self.assertEqual(expected, actual.to_array())


if __name__ == '__main__':
    unittest.main()
