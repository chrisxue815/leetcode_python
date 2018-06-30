import unittest
import utils


# O(n) time. O(1) space. Space-optimized DP.
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = -0x80000000
        sell = prev_sell = 0

        for price in prices:
            curr_sell = sell
            sell = max(sell, buy + price)
            buy = max(buy, prev_sell - price)
            prev_sell = curr_sell

        return sell


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p309.json').test_cases

        for case in cases:
            actual = Solution().maxProfit(case.prices)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
