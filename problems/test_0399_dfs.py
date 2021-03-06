import collections
import unittest
import utils


def calc(graph, visited, a, c):
    if a in visited:
        return None
    visited.add(a)

    successors = graph[a]
    a_to_c = successors.get(c, None)
    if a_to_c is not None:
        return a_to_c

    for b, a_to_b in successors.items():
        b_to_c = calc(graph, visited, b, c)
        if b_to_c is not None:
            return a_to_b * b_to_c

    return None


# O(V+E) time. O(V) space. DFS.
class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        result = []
        graph = collections.defaultdict(dict)

        for (a, b), a_to_b in zip(equations, values):
            graph[a][b] = a_to_b
            graph[b][b] = 1.0
            if a_to_b:
                graph[b][a] = 1.0 / a_to_b
                graph[a][a] = 1.0

        for a, b in queries:
            visited = set()
            a_to_b = calc(graph, visited, a, b)

            if a_to_b is None:
                a_to_b = -1.0

            result.append(a_to_b)

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().calcEquation(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
