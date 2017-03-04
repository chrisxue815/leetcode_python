import sys
import unittest
from tree import TreeNode


class Solution(object):

    def __init__(self):
        self.prev_val = -sys.maxint - 1  # assuming minint is not in the tree
        self.prev_count = -1
        self.max_vals = []
        self.max_count = 0

    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self._find_mode(root)
        self._check_prev()
        return self.max_vals

    def _find_mode(self, node):
        if not node:
            return

        self._find_mode(node.left)

        if node.val == self.prev_val:
            self.prev_count += 1
        else:
            self._check_prev()
            self.prev_val = node.val
            self.prev_count = 1

        self._find_mode(node.right)

    def _check_prev(self):
        if self.max_count < self.prev_count:
            self.max_count = self.prev_count
            del self.max_vals[:]
            self.max_vals.append(self.prev_val)
        elif self.max_count == self.prev_count:
            self.max_vals.append(self.prev_val)


class Test(unittest.TestCase):

    def test(self):
        root = TreeNode.from_array([1, None, 2, 2])
        self.assertEqual(
            Solution().findMode(root),
            [2])

        root = TreeNode.from_array([1, 1, 2, None, None, 2])
        self.assertEqual(
            Solution().findMode(root),
            [1, 2])


if __name__ == '__main__':
    unittest.main()
