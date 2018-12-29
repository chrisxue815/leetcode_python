import unittest
from tree import TreeNode


def _kth(node, k, index):
    if not node:
        return index, None

    index, result = _kth(node.left, k, index)
    if index == k:
        return index, result

    index += 1
    if index == k:
        return index, node.val

    return _kth(node.right, k, index)


# O(n) time. O(h) space. Recursive, pure functional, in-order traversal.
# Optimization: self-balancing BST
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        return _kth(root, k, 0)[1]


class Test(unittest.TestCase):
    def test(self):
        self._test([4, 2, 6, 1, 3, 5, 7], 6, 6)

    def _test(self, root, k, expected):
        root = TreeNode.from_array(root)
        actual = Solution().kthSmallest(root, k)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
