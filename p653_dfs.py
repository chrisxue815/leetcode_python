import unittest
from tree import TreeNode


class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """

        def find_val(node, val, exclude):
            if not node:
                return False
            if node.val == val and node is not exclude:
                return True
            if node.val >= val and find_val(node.left, val, exclude):
                return True
            return node.val <= val and find_val(node.right, val, exclude)

        def find_complement(node):
            if not node:
                return False
            if find_val(root, k - node.val, node):
                return True
            return find_complement(node.left) or find_complement(node.right)

        return find_complement(root)


class Test(unittest.TestCase):
    def test(self):
        self._test([5, 3, 6, 2, 4, None, 7], 9, True)
        self._test([5, 3, 6, 2, 4, None, 7], 28, False)
        self._test([1], 2, False)

    def _test(self, root, k, expected):
        root = TreeNode.from_array(root)
        actual = Solution().findTarget(root, k)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
