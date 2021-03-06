import unittest

import utils


def bit_counts(r):
    counts = [0] * (r + 1)
    for x in range(1, r + 1):
        counts[x] = counts[x >> 1] + (x & 1)
    return counts


# O(n) time. O(n) space. DP.
class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        counts = bit_counts(R)
        # let n = [2, 3, 5, 7, 11, 13, 17, 19]
        # the n-th bit of 665772 is set
        return sum((665772 >> counts[num]) & 1 for num in range(L, R + 1))


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().countPrimeSetBits(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
