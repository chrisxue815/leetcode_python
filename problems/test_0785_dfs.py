import unittest
from typing import List

import utils


# O(V+E) time. O(V) space. DFS.
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        groups = [-1] * len(graph)

        def dfs(a, a_group):
            groups[a] = a_group
            b_group = 1 - a_group

            for b in graph[a]:
                if groups[b] == b_group:
                    continue
                if groups[b] == a_group or not dfs(b, b_group):
                    return False

            return True

        for i in range(len(graph)):
            if groups[i] == -1 and not dfs(i, 0):
                return False

        return True


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
