import collections
import unittest
from typing import List

import utils


def build_graph(intervals):
    graph = collections.defaultdict(list)

    for i, a in enumerate(intervals):
        for j in range(i + 1, len(intervals)):
            b = intervals[j]
            if a[0] <= b[1] and b[0] <= a[1]:
                graph[a].append(b)
                graph[b].append(a)

    return graph


# O(n^2) time. O(n) space. Graph, DFS.
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = [tuple(interval) for interval in intervals]
        graph = build_graph(intervals)
        result = []
        visited = set()

        def dfs(curr, merged):
            if curr in visited:
                return
            visited.add(curr)

            merged[0] = min(merged[0], curr[0])
            merged[1] = max(merged[1], curr[1])

            for neighbor in graph[curr]:
                dfs(neighbor, merged)

        for start in intervals:
            if start in visited:
                continue

            merged = list(start)
            dfs(start, merged)
            result.append(merged)

        return result


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution, process_result=lambda result: sorted(result))


if __name__ == '__main__':
    unittest.main()
