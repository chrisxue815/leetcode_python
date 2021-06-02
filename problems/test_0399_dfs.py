import collections
import unittest
from typing import List

import utils


def calc(graph, visited, a, c):
    if a in visited:
        return None
    visited.add(a)

    successors = graph[a]
    a_to_c = successors.get(c, None)
    if a_to_c is not None:
        return a_to_c

    for b, a_to_b in successors.items():
        b_to_c = calc(graph, visited, b, c)
        if b_to_c is not None:
            return a_to_b * b_to_c

    return None


# O(V+E) time. O(V) space. DFS.
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        result = []
        graph = collections.defaultdict(dict)

        for (a, b), a_to_b in zip(equations, values):
            graph[a][b] = a_to_b
            graph[b][b] = 1.0
            if a_to_b:
                graph[b][a] = 1.0 / a_to_b
                graph[a][a] = 1.0

        for a, b in queries:
            visited = set()
            a_to_b = calc(graph, visited, a, b)

            if a_to_b is None:
                a_to_b = -1.0

            result.append(a_to_b)

        return result


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
