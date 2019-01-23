import unittest
import utils


# O(n^2) time. O(1) space. Iteration.
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = len(s)

        def extendPalindrome(lo, hi):
            while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
                lo -= 1
                hi += 1
            return (hi - lo + 1) // 2 - 1

        for i in xrange(len(s)):
            result += extendPalindrome(i - 1, i + 1)
            result += extendPalindrome(i - 1, i)

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().countSubstrings(**vars(case.args))
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
