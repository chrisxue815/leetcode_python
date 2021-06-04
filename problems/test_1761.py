import unittest
from typing import List

import utils


class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        result = 0x7FFFFFFF
        graph = [set() for _ in range(n + 1)]
        degrees = [0] * (n + 1)

        for a, b, in edges:
            graph[a].add(b)
            graph[b].add(a)
            degrees[a] += 1
            degrees[b] += 1

        sorted_degrees = sorted((a_degree, a) for a, a_degree in enumerate(degrees))

        for a_degree, a in sorted_degrees:
            if a_degree * 3 - 6 >= result:
                break

            a_neighbors = graph[a]
            for b in a_neighbors:
                b_neighbors = graph[b]
                for c in a_neighbors & b_neighbors:
                    result = min(result, len(a_neighbors) + len(b_neighbors) + len(graph[c]) - 6)

        return result if result != 0x7FFFFFFF else -1


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
