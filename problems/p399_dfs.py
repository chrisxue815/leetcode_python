import collections
import unittest
import utils


def calc(graph, visited, a, c):
    adj = graph[a]
    a_to_c = adj.get(c, None)

    if a_to_c is not None:
        return a_to_c

    for b, a_to_b in adj.iteritems():
        if b in visited:
            continue
        visited.add(b)
        b_to_c = calc(graph, visited, b, c)
        if b_to_c is not None:
            return a_to_b * b_to_c

    return None


# O(V+E) time. O(V) space. DFS.
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = collections.defaultdict(dict)

        for (a, b), a_to_b in zip(equations, values):
            graph[a][b] = a_to_b
            graph[b][a] = 1 / a_to_b

        result = []

        for a, b in queries:
            visited = {a}
            a_to_b = calc(graph, visited, a, b)
            if a_to_b is None:
                a_to_b = -1.0
            result.append(a_to_b)

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p399.json').test_cases

        for case in cases:
            actual = Solution().calcEquation(case.equations, case.values, case.queries)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
