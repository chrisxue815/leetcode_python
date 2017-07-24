import unittest
from tree import TreeNode


class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """

        def merge(a, b):
            if a:
                if b:
                    a.val += b.val
                    a.left = merge(a.left, b.left)
                    a.right = merge(a.right, b.right)
                    return a
                else:
                    return a
            return b

        return merge(t1, t2)


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
