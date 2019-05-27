import unittest
from tree import TreeNode, null


class Solution:

    def __init__(self):
        self.depth = -1
        self.leftmost_val = 0

    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self._find_bottomleft_value(root, 0)
        return self.leftmost_val

    def _find_bottomleft_value(self, node, depth):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not node:
            return

        if self.depth < depth:
            self.depth = depth
            self.leftmost_val = node.val

        self._find_bottomleft_value(node.left, depth + 1)
        self._find_bottomleft_value(node.right, depth + 1)


class Test(unittest.TestCase):

    def test(self):
        root = TreeNode.from_array([2, 1, 3])
        self.assertEqual(1, Solution().findBottomLeftValue(root))

        root = TreeNode.from_array([1, 2, 3, 4, null, 5, 6, null, null, 7])
        self.assertEqual(7, Solution().findBottomLeftValue(root))


if __name__ == '__main__':
    unittest.main()
