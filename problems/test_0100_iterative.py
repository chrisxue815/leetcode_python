import unittest
from tree import TreeNode


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        stack = []
        while p or stack:
            if (p is None) != (q is None):
                return False
            if p:
                if p.val != q.val:
                    return False
                stack.append((p.right, q.right))
                p, q = p.left, q.left
            else:
                p, q = stack.pop()
        return q is None


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 3, 4], [1, 2, 3, 4], True)
        self._test([1, 2, 3, 4], [1, 2, 3, 5], False)
        self._test([1, 2, 3, 4], [], False)

    def _test(self, p, q, expected):
        p = TreeNode.from_array(p)
        q = TreeNode.from_array(q)

        actual = Solution().isSameTree(p, q)
        self.assertEqual(expected, actual)

        actual = Solution().isSameTree(q, p)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
