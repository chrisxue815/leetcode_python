import unittest

import utils


# O(1) time. O(1) space. Bit manipulation.
class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        tmp = N
        shift = 0

        if tmp > 0xffff:
            tmp >>= 16
            shift += 16
        if tmp > 0xff:
            tmp >>= 8
            shift += 8
        if tmp > 0xf:
            tmp >>= 4
            shift += 4
        if tmp > 3:
            tmp >>= 2
            shift += 2
        if tmp > 1:
            tmp >>= 1
            shift += 1

        mask = (1 << (shift + 1)) - 1

        return (~N) & mask


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().bitwiseComplement(**case.args._asdict())
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
