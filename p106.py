import unittest
from tree import TreeNode, null


class Solution(object):

    def __init__(self):
        self.inorder = None
        self.postorder = None

    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        self.inorder = inorder
        self.postorder = postorder
        return self._build(len(postorder) - 1, 0, len(inorder))

    def _build(self, postorder_index, inorder_left, inorder_right):
        if inorder_left >= inorder_right:
            return None

        root_val = self.postorder[postorder_index]

        for i in xrange(inorder_left, inorder_right):
            if self.inorder[i] == root_val:
                break

        root = TreeNode(root_val)
        root.right = self._build(postorder_index - 1, i + 1, inorder_right)

        right_tree_size = inorder_right - i - 1
        root.left = self._build(postorder_index - right_tree_size - 1,
                                inorder_left, i)
        return root


class Test(unittest.TestCase):

    def test(self):
        self._test(
            [1, 2, 3, 4, 5, 6, 7],
            [1, 3, 2, 5, 7, 6, 4],
            [4, 2, 6, 1, 3, 5, 7])

        self._test(
            [1, 2, 3, 4],
            [3, 2, 1, 4],
            [4, 1, null, null, 2, null, 3])

    def _test(self, inorder, postorder, levelorder):
        self.assertEqual(
            Solution().buildTree(inorder, postorder).to_array(),
            levelorder)


if __name__ == '__main__':
    unittest.main()
