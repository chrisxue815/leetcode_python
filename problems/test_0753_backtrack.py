import itertools
import unittest

import utils


# O(k * k^n) time. O(n * k^n) space. Math, combinatorics, backtracking.
class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        result = []
        visited = set()
        target_count = k ** n

        def dfs(prefix):
            if len(visited) == target_count:
                return True

            for i in range(k):
                pw = prefix + str(i)
                if pw not in visited:
                    visited.add(pw)
                    if dfs(pw[1:]):
                        result.append(str(i))
                        return True
                    visited.remove(pw)

            return False

        initial_prefix = '0' * (n - 1)
        dfs(initial_prefix)

        return initial_prefix + ''.join(reversed(result))


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
