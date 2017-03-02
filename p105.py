import unittest
from tree import TreeNode


class Solution(object):

    def __init__(self):
        self.preorder = None
        self.inorder = None

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        self.preorder = preorder
        self.inorder = inorder
        return self._build(0, 0, len(inorder))

    def _build(self, preorder_index, inorder_left, inorder_right):
        if inorder_left >= inorder_right:
            return None

        root_val = self.preorder[preorder_index]
        for i in xrange(inorder_left, inorder_right):
            if self.inorder[i] == root_val:
                break

        root = TreeNode(root_val)
        root.left = self._build(preorder_index + 1, inorder_left, i)
        root.right = self._build(preorder_index + i - inorder_left + 1,
                                 i + 1, inorder_right)
        return root


class Test(unittest.TestCase):

    def test(self):
        self._test(
            [4, 2, 1, 3, 6, 5, 7],
            [1, 2, 3, 4, 5, 6, 7],
            [4, 2, 6, 1, 3, 5, 7])

    def _test(self, preorder, inorder, levelorder):
        self.assertEqual(
            Solution().buildTree(preorder, inorder).to_array(),
            levelorder)


if __name__ == '__main__':
    unittest.main()
