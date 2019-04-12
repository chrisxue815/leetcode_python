import unittest

import utils


# O(n) time. O(n) space. DP.
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [0] * n
        ugly[0] = 1
        i2 = i3 = i5 = 0
        nxt2, nxt3, nxt5 = 2, 3, 5

        for i in range(1, n):
            nxt = min(nxt2, nxt3, nxt5)
            ugly[i] = nxt

            if nxt == nxt2:
                i2 += 1
                nxt2 = ugly[i2] * 2
            if nxt == nxt3:
                i3 += 1
                nxt3 = ugly[i3] * 3
            if nxt == nxt5:
                i5 += 1
                nxt5 = ugly[i5] * 5

        return ugly[-1]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().nthUglyNumber(**case.args._asdict())
            self.assertEqual(case.expected, actual, msg=case.args)


if __name__ == '__main__':
    unittest.main()
