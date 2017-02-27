import Queue
import unittest
from tree import TreeNode, null


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        right_view = []
        q = Queue.Queue()
        q.put(root)

        while not q.empty():
            qsize = q.qsize() - 1
            node = self._pop_and_push_subtree(q)
            right_view.append(node.val)

            for _ in xrange(qsize):
                self._pop_and_push_subtree(q)

        return right_view

    def _pop_and_push_subtree(self, q):
        node = q.get()
        if node.right != None:
            q.put(node.right)
        if node.left != None:
            q.put(node.left)
        return node


class Test(unittest.TestCase):

    def test(self):
        self._test([4, 2, 6, 1, 3, 5, 7, 0])

    def _test(self, vals):
        root = TreeNode.from_array(vals)
        self.assertEqual(Solution().rightSideView(root), [4, 6, 7, 0])


if __name__ == '__main__':
    unittest.main()
