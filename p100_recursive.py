import unittest
from tree import TreeNode


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return p and q and p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) \
               or not p and not q


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 3, 4], [1, 2, 3, 4], True)
        self._test([1, 2, 3, 4], [1, 2, 3, 5], False)
        self._test([1, 2, 3, 4], [], False)

    def _test(self, p, q, expected):
        p = TreeNode.from_array(p)
        q = TreeNode.from_array(q)
        actual = Solution().isSameTree(p, q)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
