import unittest
from tree import TreeNode


class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1:
            return t2
        if not t2:
            return t1

        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)

        return t1


class Test(unittest.TestCase):
    def test(self):
        self._test(
            [1, 3, 2, 5],
            [2, 1, 3, None, 4, None, 7],
            [3, 4, 5, 5, 4, None, 7])

    def _test(self, t1, t2, expected):
        t1 = TreeNode.from_array(t1)
        t2 = TreeNode.from_array(t2)
        actual = Solution().mergeTrees(t1, t2)
        actual = actual.to_array()
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
