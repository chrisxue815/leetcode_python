import unittest
import utils


# O(n) time. O(1) space. Greedy.
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        result = 0
        lo = 0x7FFFFFFF
        hi = 0

        for price in prices:
            if price < hi - fee:
                profit = hi - lo - fee
                if profit > 0:
                    result += profit
                lo = hi = price
            elif price < lo:
                lo = hi = price
            elif price > hi:
                hi = price

        profit = hi - lo - fee
        if profit > 0:
            result += profit

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p714.json').test_cases

        for case in cases:
            actual = Solution().maxProfit(case.prices, case.fee)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
