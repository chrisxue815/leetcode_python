import collections
import unittest
from typing import List

import utils


# O(V+E) time. O(V) space. BFS.
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        in_degrees = [0] * numCourses

        for successor, predecessor in prerequisites:
            graph[predecessor].append(successor)
            in_degrees[successor] += 1

        q = collections.deque()

        for node, in_degree in enumerate(in_degrees):
            if in_degree == 0:
                q.append(node)

        k = 0

        while q:
            node = q.popleft()
            k += 1

            for successor in graph[node]:
                in_degrees[successor] -= 1
                if in_degrees[successor] == 0:
                    q.append(successor)

        return k == numCourses


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
