import unittest

import utils

NOT_VISITED = -1
PENDING = 0
COMPLETE = 1


# O(V+E) time. O(V) space. DFS.
class Solution(object):
    def canFinish(self, num_courses, prerequisites):
        """
        :type num_courses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[] for _ in range(num_courses)]

        for successor, predecessor in prerequisites:
            graph[predecessor].append(successor)

        visited_nodes = [NOT_VISITED] * num_courses

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

        return not any(has_cycle(node) for node in range(num_courses))


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().canFinish(**case.args._asdict())
            self.assertEqual(case.expected, actual, msg=case.args)


if __name__ == '__main__':
    unittest.main()
