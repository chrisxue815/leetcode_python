import unittest
from typing import List

import utils

NOT_VISITED = -1
PENDING = 0
COMPLETE = 1


# O(V+E) time. O(V) space. DFS.
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]

        for successor, predecessor in prerequisites:
            graph[successor].append(predecessor)

        result = []
        visited_nodes = [NOT_VISITED] * numCourses

        def try_reverse_topological_sort(node):
            if visited_nodes[node] != NOT_VISITED:
                return visited_nodes[node] == COMPLETE

            visited_nodes[node] = PENDING

            for next_node in graph[node]:
                if not try_reverse_topological_sort(next_node):
                    return False

            result.append(node)
            visited_nodes[node] = COMPLETE

            return True

        for node in range(numCourses):
            if not try_reverse_topological_sort(node):
                return []

        return result


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution, check_result=self.check_result)

    def check_result(self, args, actual, msg):
        self.assertIn(actual, args.expected, msg)


if __name__ == '__main__':
    unittest.main()
