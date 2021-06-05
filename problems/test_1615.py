import itertools
import unittest
from typing import List

import utils


# Average O(V+E) time, worst case O(V^2+E) time. O(V+E) space.
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = [set() for _ in range(n)]

        for a, b in roads:
            graph[a].add(b)
            graph[b].add(a)

        count1 = 0
        cities1 = []
        count2 = 0
        cities2 = []

        for a in range(n):
            a_degree = len(graph[a])
            if a_degree > count1:
                count2 = count1
                cities2 = cities1
                count1 = a_degree
                cities1 = [a]
            elif a_degree == count1:
                cities1.append(a)
            elif a_degree > count2:
                count2 = a_degree
                cities2 = [a]
            elif a_degree == count2:
                cities2.append(a)

        if len(cities1) >= 2:
            for a, b in itertools.combinations(cities1, 2):
                if b not in graph[a]:
                    return count1 << 1
            return (count1 << 1) - 1

        a_neighbors = graph[cities1[0]]
        for b in cities2:
            if b not in a_neighbors:
                return count1 + count2
        return count1 + count2 - 1


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
