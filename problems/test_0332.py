import collections
import heapq
import unittest
from typing import List

import utils


# O(V+E) time. O(V) space. Eulerian path, Hierholzer's algorithm, DFS.
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)

        for origin, dest in tickets:
            heapq.heappush(graph[origin], dest)

        route = []

        def dfs(node):
            successors = graph[node]
            while successors:
                dfs(heapq.heappop(successors))
            route.append(node)

        dfs('JFK')
        route.reverse()
        return route


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
