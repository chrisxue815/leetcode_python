import sys
import unittest
from tree import TreeNode, null


class Codec(object):

    def __init__(self):
        self.tree = ''

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        self._preorder(root)
        return self.tree[:-1]

    def _preorder(self, node):
        if not node:
            return
        self.tree += str(node.val) + ' '
        self._preorder(node.left)
        self._preorder(node.right)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        rootParent = TreeNode(sys.maxint)
        parent = rootParent
        stack = []

        for val in data.split():
            val = int(val)
            node = TreeNode(val)

            if val < parent.val:
                parent.left = node
            else:
                while parent.val <= val:
                    parent = stack.pop()

                stack.append(parent)
                parent = parent.left

                while parent.right:
                    stack.append(parent)
                    parent = parent.right

                parent.right = node

            stack.append(parent)
            parent = node

        return rootParent.left


class Test(unittest.TestCase):

    def test(self):
        self._test([4, 2, 6, 1, 3, 5, 7])

    def _test(self, vals):
        root = TreeNode.from_array(vals)
        codec = Codec()
        self.assertEqual(vals, codec.deserialize(codec.serialize(root)).to_array())


if __name__ == '__main__':
    unittest.main()
