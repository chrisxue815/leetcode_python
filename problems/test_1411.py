import unittest

import utils


# O(n) time. O(1) space. DP.
class Solution:
    def numOfWays(self, n: int) -> int:
        a121 = 6
        a123 = 6
        mod = 10 ** 9 + 7
        for i in range(n - 1):
            b121 = (a121 * 3 + a123 * 2) % mod
            b123 = (a121 * 2 + a123 * 2) % mod
            a121 = b121
            a123 = b123
        return (a121 + a123) % mod


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
