import unittest
from tree import TreeNode, null


class Solution(object):

    def __init__(self):
        self.sum = 0

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        self._sum(root, 0)
        return self.sum

    def _sum(self, node, parent_sum):
        parent_sum += node.val

        if not node.left and not node.right:
            self.sum += parent_sum
            return

        parent_sum *= 10
        if node.left:
            self._sum(node.left, parent_sum)
        if node.right:
            self._sum(node.right, parent_sum)


class Test(unittest.TestCase):

    def test(self):
        self._test([1, 2, 3])

    def _test(self, vals):
        root = TreeNode.from_array(vals)
        self.assertEqual(Solution().sumNumbers(root), 25)


if __name__ == '__main__':
    unittest.main()
