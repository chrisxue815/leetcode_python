import unittest
from tree import TreeNode


class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def make_bst_greater_again(node, sum_):
            if not node:
                return sum_
            node.val += make_bst_greater_again(node.right, sum_)
            return make_bst_greater_again(node.left, node.val)

        make_bst_greater_again(root, 0)
        return root


class Test(unittest.TestCase):
    def test_serialize(self):
        self._test([5, 2, 13], [18, 20, 13])

    def _test(self, vals, expected):
        root = TreeNode.from_array(vals)
        actual = Solution().convertBST(root)
        actual = actual.to_array()
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
