import Queue
import unittest
from tree import TreeNode, null


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        vals = []
        que = Queue.Queue()
        que.put(root)

        while not que.empty():
            node = que.get()

            if not node:
                vals.append('#')
            else:
                vals.append(node.val)
                que.put(node.left)
                que.put(node.right)

        return ' '.join(map(str, vals))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        root_parent = TreeNode(0)
        que = Queue.Queue()
        que.put((root_parent, 'l'))

        for val in data.split(' '):
            (parent, leftOrRight) = que.get()

            if val == '#':
                continue

            node = TreeNode(int(val))

            if leftOrRight == 'l':
                parent.left = node
            else:
                parent.right = node

            que.put((node, 'l'))
            que.put((node, 'r'))

        return root_parent.left


class Test(unittest.TestCase):
    def test_serialize(self):
        self._test([])
        self._test([1, 2, 3, 4, 5, 6, 7])
        self._test([1, 2, 3, null, 4, 5])

    def _test(self, vals):
        root = TreeNode.from_array(vals)
        codec = Codec()
        self.assertEqual(vals, TreeNode.to_array_static(codec.deserialize(codec.serialize(root))))


if __name__ == '__main__':
    unittest.main()
