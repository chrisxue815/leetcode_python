import fractions
import unittest

import utils


# O(n) time. O(1) space. Math.
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        len_gcd = fractions.gcd(len(str1), len(str2))
        gcd = str1[:len_gcd]

        if gcd == str2[:len_gcd] \
                and str1 == gcd * (len(str1) // len_gcd) \
                and str2 == gcd * (len(str2) // len_gcd):
            return gcd
        else:
            return ''


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().gcdOfStrings(**case.args._asdict())
            self.assertEqual(case.expected, actual, msg=case.args)


if __name__ == '__main__':
    unittest.main()
