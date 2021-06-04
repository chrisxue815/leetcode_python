import unittest
from typing import List

import utils


# O(V+E) time. O(V) space. Graph, DFS, backtracking.
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        visited = [False] * len(graph)
        path = [0]
        paths = []

        def dfs(i):
            if i == len(graph) - 1:
                paths.append(list(path))
                return

            for j in graph[i]:
                if visited[j]:
                    continue

                visited[j] = True
                path.append(j)

                dfs(j)

                path.pop()
                visited[j] = False

        dfs(0)
        return paths


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
