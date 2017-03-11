import unittest
from tree import TreeNode


def _find_predecessor(root):
    cur = root.left
    if not cur:
        return None
    right = cur.right
    while right and right is not root:
        cur = right
        right = cur.right
    return cur


def _stop_morris(root):
    while root:
        predecessor = _find_predecessor(root)
        if predecessor and predecessor.right is root:
            predecessor.right = None
        root = root.right


class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        prev = None
        error1 = None
        error2 = None

        while root:
            predecessor = _find_predecessor(root)

            if not predecessor or predecessor.right is root:
                if prev:
                    if prev.val > root.val:
                        if error1:
                            root.val, error1.val = error1.val, root.val
                            _stop_morris(root)
                            return
                        else:
                            error1 = prev
                            error2 = root
                    elif error1 and root.val > error1.val:
                        error1.val, error2.val = error2.val, error1.val
                        _stop_morris(root)
                        return

                prev = root

            if not predecessor:
                root = root.right
            elif predecessor.right is root:
                predecessor.right = None
                root = root.right
            else:
                predecessor.right = root
                root = root.left

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
        self.assertEqual(root.to_array(), expected)


if __name__ == '__main__':
    unittest.main()
