import unittest
from tree import TreeNode


class Solution(object):
    def countNodes(self, root):
        if not root:
            return 0

        height = self._height(root)
        return self._count(root, height)

    def _count(self, root, height):
        if height == 0:
            return 1

        left_height = height - 1
        right_height = self._height(root.right)

        if left_height == right_height:
            return (1 << (left_height + 1)) + self._count(root.right, right_height)
        else:
            return (1 << right_height + 1) + self._count(root.left, left_height)

    def _height(self, root):
        h = -1
        while root:
            h += 1
            root = root.left
        return h


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 3, 4, 5])
        self._test([1, 2, 3, 4, 5, 6])
        self._test([1, 2, 3, 4, 5, 6, 7])

    def _test(self, vals):
        root = TreeNode.from_array(vals)
        self.assertEqual(len(vals), Solution().countNodes(root))


if __name__ == '__main__':
    unittest.main()
