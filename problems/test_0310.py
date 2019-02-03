import collections
import heapq
import unittest
import utils


# O(V+E) time. O(V) space. BFS.
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        graph = [set() for _ in range(n)]

        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        leaves = []

        for node, successors in enumerate(graph):
            if len(successors) <= 1:
                leaves.append(node)

        while n > 2:
            n -= len(leaves)
            new_leaves = []

            for leaf in leaves:
                successor = graph[leaf].pop()
                graph[successor].remove(leaf)

                if len(graph[successor]) == 1:
                    new_leaves.append(successor)

            leaves = new_leaves

        return leaves


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().findMinHeightTrees(**vars(case.args))
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
