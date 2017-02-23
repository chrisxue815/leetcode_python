import Queue
import unittest


null = None


class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def setleft(self, left):
        self.left = left
        return self

    def setright(self, right):
        self.right = right
        return self

    def setchildren(self, left, right):
        self.left = left
        self.right = right
        return self

    def to_array(self):
        """
        Serializes binary tree in Leetcode style using level order traversal (BFS)
        :rtype: List[int or None]
        """
        vals = []
        que = Queue.Queue()
        que.put(self)

        while not que.empty():
            node = que.get()

            if node is None:
                vals.append(None)
            else:
                vals.append(node.val)
                que.put(node.left)
                que.put(node.right)

        while not vals[-1]:
            vals.pop()

        return vals

    @staticmethod
    def from_array(vals):
        """
        Deserializes binary tree from Leetcode-style representation
        :type vals: List[int or None]
        :rtype: TreeNode
        """
        rootParent = TreeNode(0)
        que = Queue.Queue()
        que.put((rootParent, 'l'))

        for val in vals:
            (parent, leftOrRight) = que.get()

            if val is None:
                continue

            node = TreeNode(val)

            if leftOrRight == 'l':
                parent.left = node
            else:
                parent.right = node

            que.put((node, 'l'))
            que.put((node, 'r'))

        return rootParent.left


class Test(unittest.TestCase):

    def test_to_array(self):
        root = TreeNode(1) \
            .setleft(TreeNode(2).setright(TreeNode(3))) \
            .setright(TreeNode(4).setleft(TreeNode(5)))
        self.assertEqual(root.to_array(), [1, 2, 4, None, 3, 5])

    def test_from_array(self):
        vals = [1, 2, 4, None, 3, 5]
        self.assertEqual(TreeNode.from_array(vals).to_array(), vals)


if __name__ == '__main__':
    unittest.main()
