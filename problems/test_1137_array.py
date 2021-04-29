import unittest

import utils


# O(n) time. O(n) space.
class Solution:
    def tribonacci(self, n: int) -> int:
        a = [0] * 38
        a[1] = 1
        a[2] = 1
        for i in range(3, n + 1):
            a[i] = a[i - 3] + a[i - 2] + a[i - 1]

        print(a)
        return a[n]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().tribonacci(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
