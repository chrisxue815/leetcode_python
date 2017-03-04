import collections
import unittest
from tree import TreeNode, null


class Solution(object):

    def __init__(self):
        self.counts = collections.Counter()

    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self._tree_sum(root)

        max_count = 0
        max_tree_sums = []

        for sum_, count in self.counts.items():
            if max_count < count:
                max_count = count
                del max_tree_sums[:]
                max_tree_sums.append(sum_)
            elif max_count == count:
                max_tree_sums.append(sum_)

        return max_tree_sums

    def _tree_sum(self, node):
        if not node:
            return 0

        left = self._tree_sum(node.left)
        right = self._tree_sum(node.right)

        sum_ = left + right + node.val
        self.counts[sum_] += 1
        return sum_


class Test(unittest.TestCase):

    def test(self):
        root = TreeNode.from_array([5, 2, -3])
        self.assertItemsEqual(
            Solution().findFrequentTreeSum(root),
            [2, -3, 4])

        root = TreeNode.from_array([5, 2, -5])
        self.assertItemsEqual(
            Solution().findFrequentTreeSum(root),
            [2])


if __name__ == '__main__':
    unittest.main()
