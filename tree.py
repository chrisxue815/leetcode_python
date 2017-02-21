import Queue
import unittest


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
        Serializes binary tree in Leetcode-style using level order traversal (BFS)
        :rtype: List[int]
        """
        nodes = []
        que = Queue.Queue()
        que.put(self)

        while not que.empty():
            node = que.get()

            if node is None:
                nodes.append(None)
            else:
                nodes.append(node.val)
                que.put(node.left)
                que.put(node.right)

        while not nodes[-1]:
            nodes.pop()

        return nodes


class Test(unittest.TestCase):

    def test(self):
        root = TreeNode(1) \
            .setleft(TreeNode(2).setright(TreeNode(3))) \
            .setright(TreeNode(4).setleft(TreeNode(5)))
        self.assertEqual(root.to_array(), [1, 2, 4, None, 3, 5])


if __name__ == '__main__':
    unittest.main()
