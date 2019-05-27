import unittest
from tree import TreeNode


def add_row(root, v, d):
    if not root:
        return
    if d != 2:
        add_row(root.left, v, d - 1)
        add_row(root.right, v, d - 1)
    else:
        node = TreeNode(v)
        node.left = root.left
        root.left = node
        node = TreeNode(v)
        node.right = root.right
        root.right = node


class Solution:
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d == 1:
            node = TreeNode(v)
            node.left = root
            return node
        add_row(root, v, d)
        return root


class Test(unittest.TestCase):
    def test(self):
        self._test(
            [4, 2, 6, 3, 1, 5],
            1, 2,
            [4, 1, 1, 2, None, None, 6, 3, 1, 5]
        )
        self._test(
            [4, 2, None, 3, 1],
            1, 3,
            [4, 2, None, 1, 1, 3, None, None, 1]
        )
        self._test(
            [1, 2, 3],
            1, 1,
            [1, 1, None, 2, 3]
        )

    def _test(self, root, v, d, expected):
        root = TreeNode.from_array(root)
        actual = Solution().addOneRow(root, v, d)
        actual = actual.to_array()
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
