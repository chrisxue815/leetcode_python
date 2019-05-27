import queue
import sys
import unittest
from tree import TreeNode, null


class Solution:

    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        max_vals = []
        que = queue.Queue()
        que.put(root)

        while not que.empty():
            level_nodes = que.qsize()
            level_max = -sys.maxsize - 1

            for _ in range(level_nodes):
                node = que.get()

                if level_max < node.val:
                    level_max = node.val

                if node.left:
                    que.put(node.left)
                if node.right:
                    que.put(node.right)

            max_vals.append(level_max)

        return max_vals


class Test(unittest.TestCase):

    def test(self):
        root = TreeNode.from_array([1, 3, 2, 5, 3, null, 9])
        self.assertEqual([1, 3, 9], Solution().largestValues(root))


if __name__ == '__main__':
    unittest.main()
