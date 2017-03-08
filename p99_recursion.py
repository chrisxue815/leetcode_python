import unittest
from tree import TreeNode


class Solution(object):
    def __init__(self):
        self.prev = None
        self.error1 = None
        self.error2 = None

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        found = self._recover(root)
        if not found and self.error1:
            tmp = self.error1.val
            self.error1.val = self.error2.val
            self.error2.val = tmp

    def _recover(self, root):
        if not root:
            return False

        found = self._recover(root.left)
        if found:
            return True

        if self.prev:
            if self.prev.val >= root.val:
                if self.error1:
                    tmp = self.error1.val
                    self.error1.val = root.val
                    root.val = tmp
                    return True
                else:
                    self.error1 = self.prev
                    self.error2 = root
            elif self.error1 and root.val >= self.error1.val:
                tmp = self.error1.val
                self.error1.val = self.error2.val
                self.error2.val = tmp
                return True

        self.prev = root

        return self._recover(root.right)


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
        self.assertEqual(root.to_array(), expected)


if __name__ == '__main__':
    unittest.main()
