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

            if not node:
                vals.append(None)
            else:
                vals.append(node.val)
                que.put(node.left)
                que.put(node.right)

        while vals[-1] is None:
            vals.pop()

        return vals

    @staticmethod
    def to_array_static(root):
        if root:
            return root.to_array()
        else:
            return []

    @classmethod
    def from_array(cls, vals):
        """
        Deserializes binary tree from Leetcode-style representation
        :type vals: List[int or None]
        :rtype: TreeNode
        """
        root_parent = cls(0)
        que = Queue.Queue()
        que.put((root_parent, 'l'))

        for val in vals:
            (parent, leftOrRight) = que.get()

            if val is None:
                continue

            node = cls(val)

            if leftOrRight == 'l':
                parent.left = node
            else:
                parent.right = node

            que.put((node, 'l'))
            que.put((node, 'r'))

        return root_parent.left

    def to_array_inorder(self):
        """
        Serializes binary tree using inorder DFS traversal
        :rtype: List[int or None]
        """
        vals = []
        TreeNode._to_array_inorder(self, vals)
        return vals

    @staticmethod
    def _to_array_inorder(node, vals):
        if node.left:
            TreeNode._to_array_inorder(node.left, vals)

        vals.append(node.val)

        if node.right:
            TreeNode._to_array_inorder(node.right, vals)


class TreeLinkNode(TreeNode):
    def __init__(self, x):
        super(TreeLinkNode, self).__init__(x)
        self.next = None

    def to_array_bfs_fulltree(self):
        """
        Serializes FULL binary tree in Leetcode style using level order traversal (BFS)
        :rtype: List[int or None]
        """
        vals = []
        prev = curr = self

        while prev:
            while curr:
                vals.append(curr.val)
                curr = curr.next
            prev = curr = prev.left

        return vals


class Test(unittest.TestCase):
    def test_to_array(self):
        root = TreeNode(1) \
            .setleft(TreeNode(2).setright(TreeNode(3))) \
            .setright(TreeNode(4).setleft(TreeNode(5)))
        self.assertEqual(5], root.to_array(), [1, 2, 4, None, 3)

    def test_from_array(self):
        vals = [1, 2, 4, None, 3, 5]
        self.assertEqual(vals, TreeNode.from_array(vals).to_array())

    def test_to_array_inorder(self):
        vals = [4, 2, 6, 1, 3, 5, 7]
        self.assertEqual(
            TreeNode.from_array(vals).to_array_inorder(),
            [1, 2, 3, 4, 5, 6, 7])


if __name__ == '__main__':
    unittest.main()
