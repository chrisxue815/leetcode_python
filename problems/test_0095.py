import collections
import unittest
from tree import TreeNode, null


class Solution:

    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        trees = collections.defaultdict(list)
        bsts = []
        for num_nodes in range(1, n + 1):
            for rootval in range(1, n + 1):
                if num_nodes < n:
                    leftrange = range(0, num_nodes)
                else:
                    leftrange = range(rootval - 1, rootval)

                for num_left_nodes in leftrange:
                    num_right_nodes = num_nodes - num_left_nodes - 1
                    ll = rootval - num_left_nodes
                    lr = rootval - 1
                    rl = rootval + 1
                    rr = rootval + num_right_nodes
                    lefttrees = trees.get((ll, lr)) or [None]
                    righttrees = trees.get((rl, rr)) or [None]
                    treelist = trees[(ll, rr)]
                    for lefttree in lefttrees:
                        for righttree in righttrees:
                            root = TreeNode(rootval)
                            root.left = lefttree
                            root.right = righttree
                            treelist.append(root)
                            if num_nodes == n and ll == 1:
                                bsts.append(root)
        return bsts


class Test(unittest.TestCase):

    def test(self):
        self._test(
            1,
            [[1]])

        self._test(
            2,
            [[1, null, 2],
             [2, 1]])

        self._test(
            3,
            [[1, null, 2, null, 3],
             [1, null, 3, 2],
             [2, 1, 3],
             [3, 1, null, null, 2],
             [3, 2, null, 1]])

    def _test(self, n, trees):
        actualtrees = Solution().generateTrees(n)
        self.assertEqual(len(trees), len(actualtrees))
        for (expected, actual) in zip(trees, actualtrees):
            self.assertEqual(expected, actual.to_array())


if __name__ == '__main__':
    unittest.main()
