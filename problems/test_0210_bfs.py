import collections
import unittest
from typing import List

import utils


# O(V+E) time. O(V) space. BFS.
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        in_degrees = [0] * numCourses

        for successor, predecessor in prerequisites:
            graph[predecessor].append(successor)
            in_degrees[successor] += 1

        q = collections.deque()

        for node, in_degree in enumerate(in_degrees):
            if in_degree == 0:
                q.append(node)

        result = []

        while q:
            node = q.popleft()
            result.append(node)

            for successor in graph[node]:
                in_degrees[successor] -= 1
                if in_degrees[successor] == 0:
                    q.append(successor)

        return result if len(result) == numCourses else []


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution, check_result=self.check_result)

    def check_result(self, args, actual, msg):
        self.assertIn(actual, args.expected, msg)


if __name__ == '__main__':
    unittest.main()
