import collections
import fractions
import unittest
import utils


# O(n) time. O(1) space. Two pointers.
class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        lo = 0
        hi = len(s) - 1

        while True:
            while lo < hi and not s[lo].isalpha():
                lo += 1
            if lo >= hi:
                break

            while lo < hi and not s[hi].isalpha():
                hi -= 1
            if lo >= hi:
                break

            s[lo], s[hi] = s[hi], s[lo]
            lo += 1
            hi -= 1

        return ''.join(s)


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().reverseOnlyLetters(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
