import unittest
import utils


# O(n^2) time. O(n) space. DP.
class Solution:
    def numberOfArithmeticSlices(self, a):
        """
        :type a: List[int]
        :rtype: int
        """
        # Common difference
        dp = [0] * len(a)
        result = 0

        for p in range(len(a) - 1):
            q = p + 1
            dp[p] = a[q] - a[p]

        for distance in range(2, len(a)):
            for p in range(len(a) - distance):
                q = p + distance
                if dp[p] == a[q] - a[q - 1]:
                    result += 1
                else:
                    dp[p] = None

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().numberOfArithmeticSlices(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
