import unittest
import utils


# O(nk) time. O(k) space. Iteration.
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not k or len(prices) < 2:
            return 0

        k = min(k, len(prices) // 2)

        buy = [0x7FFFFFFF] * k
        profit = [0] * k

        for price in prices:
            buy[0] = min(buy[0], price)
            profit[0] = max(profit[0], price - buy[0])

            for i in xrange(1, k):
                buy[i] = min(buy[i], price - profit[i - 1])
                profit[i] = max(profit[i], price - buy[i])

        return profit[-1]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p188.json').test_cases

        for case in cases:
            actual = Solution().maxProfit(case.k, case.prices)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
