import Queue
import unittest
from tree import TreeNode, null


class Solution(object):

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        self._rob(root)
        return root.optimal

    def _rob(self, node):
        a = 0  # not robbing this node
        b = node.val  # robbing this node

        if node.left:
            self._rob(node.left)
            a += node.left.optimal
            if node.left.left:
                b += node.left.left.optimal
            if node.left.right:
                b += node.left.right.optimal

        if node.right:
            self._rob(node.right)
            a += node.right.optimal
            if node.right.left:
                b += node.right.left.optimal
            if node.right.right:
                b += node.right.right.optimal

        node.optimal = max(a, b)


class Test(unittest.TestCase):

    def test(self):
        root = TreeNode.from_array([3, 2, 3, null, 3, null, 1])
        self.assertEqual(
            Solution().rob(root),
            7)

        root = TreeNode.from_array([3, 4, 5, 1, 3, null, 1])
        self.assertEqual(
            Solution().rob(root),
            9)

        root = TreeNode.from_array([4, 1, null, 2, null, 3])
        self.assertEqual(
            Solution().rob(root),
            7)


if __name__ == '__main__':
    unittest.main()
