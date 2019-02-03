import sys
import unittest
from tree import TreeNode, null


class Solution(object):

    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return None

        root_parent = TreeNode(sys.maxsize)
        root_parent.left = root

        node, parent = self._find_node(root, root_parent, key)

        if node:
            self._delete_node(node, parent)

        return root_parent.left

    def _find_node(self, root, root_parent, key):
        while True:
            if not root:
                return None, None

            if key < root.val:
                root_parent = root
                root = root.left
            elif key > root.val:
                root_parent = root
                root = root.right
            else:
                return root, root_parent

    def _delete_node(self, node, parent):
        while True:
            if not node.left:
                if node == parent.left:
                    parent.left = node.right
                else:
                    parent.right = node.right
                return
            elif not node.right:
                if node == parent.left:
                    parent.left = node.left
                else:
                    parent.right = node.left
                return
            else:
                largest_node, parent = self._find_largest(node.left, node)
                node.val = largest_node.val
                node = largest_node

    def _find_largest(self, root, root_parent):
        while root.right:
            root_parent = root
            root = root.right
        return root, root_parent


class Test(unittest.TestCase):

    def test(self):
        self._test([5, 3, 6, 2, 4, null, 7], 3,
                   [5, 2, 6, null, 4, null, 7])
        self._test([5, 3, 6, 2, 4, null, 7], 0,
                   [5, 3, 6, 2, 4, null, 7])

    def _test(self, vals, key, expected):
        root = TreeNode.from_array(vals)
        self.assertEqual(expected, Solution().deleteNode(root, key).to_array())


if __name__ == '__main__':
    unittest.main()
