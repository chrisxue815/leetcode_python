import collections
import unittest
import utils

NOT_VISITED = -1
PENDING = 0
COMPLETE = 1


# O(V+E) time. O(V) space. BFS.
class Solution(object):
    def canFinish(self, num_courses, prerequisites):
        """
        :type num_courses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[] for _ in xrange(num_courses)]
        in_degrees = [0] * num_courses

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

        return k == num_courses


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p207.json').test_cases

        for case in cases:
            actual = Solution().canFinish(case.num_courses, case.prerequisites)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
