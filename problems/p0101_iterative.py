import unittest
from tree import TreeNode


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        q = [(root.left, root.right)]

        while q:
            next_q = []
            for left, right in q:
                if (left is None) != (right is None):
                    return False
                if left:
                    if left.val != right.val:
                        return False
                    next_q.append((left.left, right.right))
                    next_q.append((left.right, right.left))
            q = next_q

        return True


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 2, 3, 4, 4, 3], True)
        self._test([1, 2, 2, None, 3, None, 3], False)

    def _test(self, root, expected):
        root = TreeNode.from_array(root)
        actual = Solution().isSymmetric(root)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
