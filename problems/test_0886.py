import unittest
from typing import List

import utils


# O(V+E) time. O(V+E) space. Graph, DFS, coloring
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = [[] for _ in range(n + 1)]

        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)

        colors = [-1] * (n + 1)

        def dfs(cur, color):
            colors[cur] = color

            for nxt in graph[cur]:
                nxt_color = colors[nxt]
                if nxt_color == color:
                    return False
                elif nxt_color == -1:
                    if not dfs(nxt, color ^ 1):
                        return False

            return True

        for i in range(1, n + 1):
            if colors[i] == -1:
                if not dfs(i, 0):
                    return False

        return True


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
