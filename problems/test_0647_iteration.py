import unittest
import utils


# O(n^2) time. O(1) space. Iteration.
class Solution:
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

        for i in range(len(s)):
            result += extendPalindrome(i - 1, i + 1)
            result += extendPalindrome(i - 1, i)

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().countSubstrings(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
