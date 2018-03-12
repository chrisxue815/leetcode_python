import unittest
import utils


def mark_cycle(graph, in_cycle, visited, in_stack, curr):
    if in_cycle[curr]:
        return True

    if in_stack[curr]:
        in_cycle[curr] = True
        return True

    if visited[curr]:
        return False

    visited[curr] = True
    in_stack[curr] = True

    for outgoing in graph[curr]:
        if mark_cycle(graph, in_cycle, visited, in_stack, outgoing):
            in_cycle[curr] = True

    in_stack[curr] = False
    return in_cycle[curr]


class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        in_cycle = [False] * len(graph)
        visited = [False] * len(graph)
        in_stack = [False] * len(graph)

        for curr in xrange(len(graph)):
            if not visited[curr]:
                mark_cycle(graph, in_cycle, visited, in_stack, curr)

        return [i for i in xrange(len(graph)) if not in_cycle[i]]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p802.json').test_cases

        for case in cases:
            actual = Solution().eventualSafeNodes(case.graph)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
