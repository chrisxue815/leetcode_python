import unittest
import utils

NOT_VISITED = -1
PENDING = 0
COMPLETE = 1


# O(V+E) time. O(V) space. DFS.
class Solution(object):
    def findOrder(self, num_courses, prerequisites):
        """
        :type num_courses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = [[] for _ in range(num_courses)]

        for successor, predecessor in prerequisites:
            graph[successor].append(predecessor)

        result = []
        visited_nodes = [NOT_VISITED] * num_courses

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

        for node in range(num_courses):
            if not try_reverse_topological_sort(node):
                return []

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().findOrder(**vars(case.args))
            self.assertIn(actual, case.expected)


if __name__ == '__main__':
    unittest.main()
