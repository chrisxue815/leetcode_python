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

        if tmp >= 1 << 16:
            tmp >>= 16
            shift += 16
        if tmp >= 1 << 8:
            tmp >>= 8
            shift += 8
        if tmp >= 1 << 4:
            tmp >>= 4
            shift += 4
        if tmp >= 1 << 2:
            tmp >>= 2
            shift += 2
        if tmp >= 1 << 1:
            tmp >>= 1
            shift += 1

        mask = (1 << (shift + 1)) - 1

        return (~N) & mask


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().bitwiseComplement(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=case.args)


if __name__ == '__main__':
    unittest.main()
