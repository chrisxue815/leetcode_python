import unittest

import utils


# O(n^2) time. O(n^2) space. Minimax, memorization.
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        cache = [[0] * (n + 1) for _ in range(n + 1)]

        def minimax(lo, hi):
            if lo >= hi:
                return 0
            if cache[lo][hi]:
                return cache[lo][hi]

            mini = 0x7fffffff
            for x in range(lo, hi + 1):
                maxi = x + max(minimax(lo, x - 1), minimax(x + 1, hi))
                mini = min(mini, maxi)
            cache[lo][hi] = mini

            return mini

        return minimax(1, n)


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().getMoneyAmount(**case.args._asdict())
            self.assertEqual(case.expected, actual, msg=case.args)


if __name__ == '__main__':
    unittest.main()
