import unittest
import utils


# O(n) time. O(1) space. Kadane's algorithm.
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_ending_here = max_so_far = 0

        for i in xrange(1, len(prices)):
            diff = prices[i] - prices[i - 1]
            max_ending_here = max(diff, max_ending_here + diff)
            max_so_far = max(max_so_far, max_ending_here)

        return max_so_far


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p121.json').test_cases

        for case in cases:
            actual = Solution().maxProfit(case.prices)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
