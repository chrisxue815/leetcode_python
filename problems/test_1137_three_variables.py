import unittest

import utils

SEEDS = [0, 1, 1]


# O(n) time. O(1) space.
class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 2:
            return SEEDS[n]

        a, b, c = SEEDS
        for i in range(3, n + 1):
            a, b, c = b, c, a + b + c

        return c


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().tribonacci(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
