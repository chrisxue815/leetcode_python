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
        graph = [[] for _ in xrange(num_courses)]

        for successor, predecessor in prerequisites:
            graph[predecessor].append(successor)

        visited_nodes = [NOT_VISITED] * num_courses

        # See Guava Graphs.hasCycle:
        # https://github.com/google/guava/blob/master/guava/src/com/google/common/graph/Graphs.java
        def has_cycle(node):
            if visited_nodes[node] != NOT_VISITED:
                return visited_nodes[node] == PENDING

            visited_nodes[node] = PENDING

            for next_node in graph[node]:
                if has_cycle(next_node):
                    return True

            visited_nodes[node] = COMPLETE

            return False

        return not any(has_cycle(node) for node in xrange(num_courses))


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p207.json').test_cases

        for case in cases:
            actual = Solution().canFinish(case.num_courses, case.prerequisites)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
