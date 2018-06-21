import unittest
import utils


# O(n) time. O(1) space. Iteration.
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result = 0

        for i in xrange(1, len(prices)):
            result += max(0, prices[i] - prices[i - 1])

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p122.json').test_cases

        for case in cases:
            actual = Solution().maxProfit(case.prices)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
