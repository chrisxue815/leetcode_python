import unittest
from tree import TreeNode


class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        stack = []
        error1 = None
        error2 = None
        prev = None

        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()

                if prev:
                    if prev.val > root.val:
                        if error1:
                            root.val, error1.val = error1.val, root.val
                            return
                        else:
                            error1 = prev
                            error2 = root
                    elif error1 and root.val > error1.val:
                        error1.val, error2.val = error2.val, error1.val
                        return

                prev = root

                root = root.right

        if error1:
            error1.val, error2.val = error2.val, error1.val


class Test(unittest.TestCase):
    def test_serialize(self):
        self._test([0, 1], [1, 0])
        self._test([4, 2, 6, 1, 3, 5, 7], [4, 2, 6, 1, 3, 5, 7])
        self._test([4, 6, 2, 1, 3, 5, 7], [4, 2, 6, 1, 3, 5, 7])
        self._test([4, 1, 6, 2, 3, 5, 7], [4, 2, 6, 1, 3, 5, 7])
        self._test([4, 3, 6, 1, 2, 5, 7], [4, 2, 6, 1, 3, 5, 7])
        self._test([4, 5, 6, 1, 3, 2, 7], [4, 2, 6, 1, 3, 5, 7])
        self._test([4, 7, 6, 1, 3, 5, 2], [4, 2, 6, 1, 3, 5, 7])

    def _test(self, vals, expected):
        root = TreeNode.from_array(vals)
        Solution().recoverTree(root)
        self.assertEqual(expected, root.to_array())


if __name__ == '__main__':
    unittest.main()
