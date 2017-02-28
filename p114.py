import unittest
from tree import TreeNode, null


class Solution(object):

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        stack = [root]
        prev = TreeNode(0)

        while len(stack) > 0:
            curr = stack.pop()

            while curr != None:
                if curr.right != None:
                    stack.append(curr.right)
                prev.left = None
                prev.right = curr
                prev = curr
                curr = curr.left


class Test(unittest.TestCase):

    def test(self):
        self._test([1, 2, 5, 3, 4, null, 6],
                   [1, null, 2, null, 3, null, 4, null, 5, null, 6])

    def _test(self, vals, expected):
        root = TreeNode.from_array(vals)
        Solution().flatten(root)
        self.assertEqual(
            root.to_array(),
            expected)


if __name__ == '__main__':
    unittest.main()
