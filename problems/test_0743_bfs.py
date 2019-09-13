import heapq
import unittest
from typing import List

import utils


# O(V + Elog(E)) time. O(V + E) space. Graph, BFS, Dijkstra.
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = [[] for _ in range(N + 1)]

        for u, v, w in times:
            graph[u].append((v, w))

        q = [(0, K)]
        visited = [False] * (N + 1)
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

        return longest_path if num_visited == N else -1


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().networkDelayTime(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
