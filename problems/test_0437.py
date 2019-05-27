import unittest
from tree import TreeNode, null


class Solution:

    def __init__(self):
        self.sum = 0
        self.count = 0

    def pathSum(self, root, sum_):
        """
        :type root: TreeNode
        :type sum_: int
        :rtype: int
        """
        self.sum = sum_
        self._path_sum(root, [])

        return self.count

    def _path_sum(self, node, paths):
        if not node:
            return

        paths = list(paths)
        paths.append(0)

        for i, path in enumerate(paths):
            path += node.val
            paths[i] = path
            if path == self.sum:
                self.count += 1

        self._path_sum(node.left, paths)
        self._path_sum(node.right, paths)


class Test(unittest.TestCase):

    def test(self):
        root = TreeNode.from_array([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])
        self.assertEqual(3, Solution().pathSum(root, 8))

        root = TreeNode.from_array(
            [5, 4, 8, 11, null, 13, 4, 7, 2, null, null, 5, 1])
        self.assertEqual(3, Solution().pathSum(root, 22))

        root = TreeNode.from_array([1])
        self.assertEqual(1, Solution().pathSum(root, 1))


if __name__ == '__main__':
    unittest.main()
