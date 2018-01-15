import unittest
from tree import TreeNode


def _balanced(root):
    if not root:
        return True, 0
    lb, lh = _balanced(root.left)
    if not lb:
        return False, 0
    rb, rh = _balanced(root.right)
    return rb and abs(lh - rh) <= 1, max(lh, rh) + 1


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return _balanced(root)[0]


class Test(unittest.TestCase):
    def test_serialize(self):
        self._test([1, 2, 3], True)
        self._test([1, 2, 3, 4], True)
        self._test([1, 2, 3, 4, None, None, None, 5], False)
        self._test([1, 2, 3, 4, None, None, 5, 6, None, None, 7], False)

    def _test(self, root, expected):
        root = TreeNode.from_array(root)
        actual = Solution().isBalanced(root)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
