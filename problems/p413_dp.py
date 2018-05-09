import unittest
import utils


# O(n^2) time. O(n^2) space. DP.
class Solution(object):
    def numberOfArithmeticSlices(self, a):
        """
        :type a: List[int]
        :rtype: int
        """
        # Common difference
        dp = [[None] * len(a) for _ in xrange(len(a))]
        result = 0

        for p in xrange(len(a) - 1):
            q = p + 1
            dp[p][q] = a[q] - a[p]

        for distance in xrange(2, len(a)):
            for p in xrange(len(a) - distance):
                q = p + distance
                if dp[p][q - 1] == dp[q - 1][q]:
                    dp[p][q] = dp[p][q - 1]
                    result += 1
                else:
                    dp[p][q] = None

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p413.json').test_cases

        for case in cases:
            actual = Solution().numberOfArithmeticSlices(case.a)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
