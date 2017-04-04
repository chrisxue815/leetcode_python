import unittest
from tree import TreeNode


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        stack = []
        prev = None
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if prev is not None and prev >= root.val:
                    return False
                prev = root.val
                root = root.right
        return True


class Test(unittest.TestCase):
    def test(self):
        self._test([], True)
        self._test([2, 1, 3], True)
        self._test([1, 2, 3], False)
        self._test([4, 2, 6, 1, 3, 5, 7], True)
        self._test([4, 2, 7, 1, 3, 5, 7], False)

    def _test(self, vals, expected):
        root = TreeNode.from_array(vals)
        self.assertEqual(
            Solution().isValidBST(root),
            expected)


if __name__ == '__main__':
    unittest.main()
