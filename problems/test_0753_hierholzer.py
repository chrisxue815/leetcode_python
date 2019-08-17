import itertools
import unittest

import utils


# O(k^n) time. O(k^n) space. Math, combinatorics, graph, Eulerian path, Hierholzer's algorithm, DFS.
class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        digits = [str(i) for i in range(k)]

        if n == 1:
            return ''.join(digits)

        result = []
        graph = {}

        def dfs(prefix):
            suffixes = graph.get(prefix)
            if suffixes is None:
                suffixes = list(digits)
                graph[prefix] = suffixes

            while suffixes:
                suffix = suffixes.pop()
                pw = prefix + suffix
                dfs(pw[1:])

            result.append(prefix[-1])

        initial_prefix = '0' * (n - 1)
        dfs(initial_prefix)

        return initial_prefix[:-1] + ''.join(reversed(result))


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().crackSafe(**case.args.__dict__)

            digits = [str(i) for i in range(case.args.k)]
            for pw in itertools.product(digits, repeat=case.args.n):
                pw = ''.join(pw)
                self.assertIn(pw, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
