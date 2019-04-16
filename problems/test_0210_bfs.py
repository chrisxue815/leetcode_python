import collections
import unittest
import utils


# O(V+E) time. O(V) space. BFS.
class Solution(object):
    def findOrder(self, num_courses, prerequisites):
        """
        :type num_courses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = [[] for _ in range(num_courses)]
        in_degrees = [0] * num_courses

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

        return result if len(result) == num_courses else []


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().findOrder(**case.args.__dict__)
            self.assertIn(actual, case.expected, msg=case.args)


if __name__ == '__main__':
    unittest.main()
