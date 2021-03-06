import unittest
import utils

_NOT_VISITED = 0
_SAFE = 1
_UNSAFE = 2


# O(V+E) time. O(V) space. DFS.
class Solution:
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        states = [_NOT_VISITED] * len(graph)

        def is_safe(node):
            if states[node] != _NOT_VISITED:
                return states[node] == _SAFE

            states[node] = _UNSAFE

            for outgoing in graph[node]:
                if not is_safe(outgoing):
                    return False

            states[node] = _SAFE
            return True

        for i in range(len(graph)):
            if states[i] == _NOT_VISITED:
                is_safe(i)

        return [i for i in range(len(graph)) if states[i] == _SAFE]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().eventualSafeNodes(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
