import unittest
from tree import TreeNode


def _set_heights(root):
    if not root:
        return 0
    lh = _set_heights(root.left)
    rh = _set_heights(root.right)
    root.height = max(lh, rh) + 1
    return root.height


def _match(s, t):
    if not s or not t:
        return s is t
    if s.height < t.height:
        return False
    if s.height > t.height:
        return _match(s.left, t) or _match(s.right, t)
    return s.val == t.val and _match(s.left, t.left) and _match(s.right, t.right)


class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s or not t:
            return s is t

        _set_heights(s)
        _set_heights(t)

        return _match(s, t)


class Test(unittest.TestCase):
    def test(self):
        self._test([3, 4, 5, 1, 2], [4, 1, 2], True)
        self._test([3, 4, 5, 1, 2, None, None, None, None, 0], [4, 1, 2], False)

    def _test(self, s, t, expected):
        s = TreeNode.from_array(s)
        t = TreeNode.from_array(t)
        actual = Solution().isSubtree(s, t)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
