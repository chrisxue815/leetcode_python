import heapq
import unittest
from typing import List

import utils


# O(V + Elog(E)) time. O(V + E) space. Graph, BFS, Dijkstra.
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n + 1)]

        for u, v, w in times:
            graph[u].append((v, w))

        q = [(0, k)]
        visited = [False] * (n + 1)
        num_visited = 0
        longest_path = 0

        while q:
            path_len, curr = heapq.heappop(q)

            if visited[curr]:
                continue
            visited[curr] = True
            num_visited += 1

            longest_path = path_len

            for nxt, edge_len in graph[curr]:
                if not visited[nxt]:
                    heapq.heappush(q, (path_len + edge_len, nxt))

        return longest_path if num_visited == n else -1


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
