import unittest
from tree import TreeNode, null


class Solution(object):

    def __init__(self):
        self.paths = []

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []

        self._binary_tree_paths(root, '')
        return self.paths

    def _binary_tree_paths(self, node, path):
        path += str(node.val)

        if not node.left and not node.right:
            self.paths.append(path)
        else:
            path += '->'
            if node.left:
                self._binary_tree_paths(node.left, path)
            if node.right:
                self._binary_tree_paths(node.right, path)


class Test(unittest.TestCase):

    def test(self):
        root = TreeNode.from_array([1, 2, 3, null, 5])
        self.assertEqual(["1->2->5", "1->3"], Solution().binaryTreePaths(root))


if __name__ == '__main__':
    unittest.main()
