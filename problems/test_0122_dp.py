import unittest
import utils


# O(n) time. O(1) space. Space-optimized DP.
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sell = 0
        buy = -0x80000000

        for price in prices:
            sell = max(sell, buy + price)
            buy = max(buy, sell - price)

        return sell


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().maxProfit(**vars(case.args))
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
