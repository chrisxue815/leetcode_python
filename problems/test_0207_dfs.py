import unittest
from typing import List

import utils

NOT_VISITED = -1
PENDING = 0
COMPLETE = 1


# O(V+E) time. O(V) space. DFS.
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]

        for successor, predecessor in prerequisites:
            graph[predecessor].append(successor)

        visited_nodes = [NOT_VISITED] * numCourses

        # See Guava Graphs.hasCycle():
        # https://github.com/google/guava/blob/674148d9d7a99c450fec9751edb9f826bc3f5784/guava/src/com/google/common/graph/Graphs.java#L56
        def has_cycle(node):
            if visited_nodes[node] != NOT_VISITED:
                return visited_nodes[node] == PENDING

            visited_nodes[node] = PENDING

            for next_node in graph[node]:
                if has_cycle(next_node):
                    return True

            visited_nodes[node] = COMPLETE

            return False

        return not any(has_cycle(node) for node in range(numCourses))


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
