import unittest
from tree import TreeNode, null


class Solution(object):

    def __init__(self):
        self.sum = 0
        self.paths = []

    def pathSum(self, root, sum_):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        self.sum = sum_
        self._path_sum(root, 0, [])
        return self.paths

    def _path_sum(self, node, sum_, path):
        sum_ += node.val
        path = list(path)
        path.append(node.val)

        if node.left is None and node.right is None:
            if sum_ == self.sum:
                self.paths.append(path)
        else:
            if node.left != None:
                self._path_sum(node.left, sum_, path)
            if node.right != None:
                self._path_sum(node.right, sum_, path)


class Test(unittest.TestCase):

    def test(self):
        self._test([5, 4, 8, 11, null, 13, 4, 7, 2, null, null, 5, 1],
                   22,
                   [[5, 4, 11, 2], [5, 8, 4, 5]])

    def _test(self, vals, sum_, expected):
        root = TreeNode.from_array(vals)
        self.assertEqual(
            Solution().pathSum(root, sum_),
            expected)


if __name__ == '__main__':
    unittest.main()
