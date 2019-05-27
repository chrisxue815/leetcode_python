import unittest
from tree import TreeNode, null


class Solution:

    def __init__(self):
        self.pval = 0
        self.qval = 0

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p.val > q.val:
            p, q = q, p

        self.pval = p.val
        self.qval = q.val

        return self._lowest_common_ancestor(root)

    def _lowest_common_ancestor(self, node):
        if self.pval <= node.val:
            if self.qval >= node.val:
                return node
            else:
                return self._lowest_common_ancestor(node.left)
        else:
            return self._lowest_common_ancestor(node.right)


class Test(unittest.TestCase):

    def test(self):
        root = TreeNode.from_array([6, 2, 8, 0, 4, 7, 9, null, null, 3, 5])
        self.assertEqual(6, Solution().lowestCommonAncestor(root, TreeNode(2), TreeNode(8)).val)


if __name__ == '__main__':
    unittest.main()
