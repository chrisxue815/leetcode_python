import Queue
import unittest
from tree import TreeNode, null


class Solution(object):

    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        curr_level = 0
        curr_max = root.val
        max_vals = []

        que = Queue.Queue()
        que.put((root, 0))

        while not que.empty():
            node, level = que.get()

            if curr_level != level:
                curr_level = level
                max_vals.append(curr_max)
                curr_max = node.val
            elif curr_max < node.val:
                curr_max = node.val

            if node.left != None:
                que.put((node.left, level + 1))
            if node.right != None:
                que.put((node.right, level + 1))

        max_vals.append(curr_max)

        return max_vals


class Test(unittest.TestCase):

    def test(self):
        root = TreeNode.from_array([1, 3, 2, 5, 3, null, 9])
        self.assertEqual(
            Solution().largestValues(root),
            [1, 3, 9])


if __name__ == '__main__':
    unittest.main()
