import itertools
import unittest
import utils


def compute_index(needs):
    return sum(item_need << (i * 3) for i, item_need in enumerate(needs))


# O(n*m^n) time. O(2^(3*m)) space. Space-optimized DP.
class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        n = len(price)
        dp = [0] * (compute_index(needs) + 1)
        all_needs = [range(need + 1) for need in needs]

        for need in itertools.product(*all_needs):
            market_price = sum(price[i] * need[i] for i in xrange(n))
            dp[compute_index(need)] = market_price

        for offer in special:
            market_price = sum(price[i] * offer[i] for i in xrange(n))
            offer_price = offer[-1]
            if market_price <= offer_price:
                continue

            offer_index = compute_index(offer[:-1])
            all_needs = [range(offer[i], needs[i] + 1) for i in xrange(n)]

            for curr_needs in itertools.product(*all_needs):
                curr_index = compute_index(curr_needs)
                dp[curr_index] = min(dp[curr_index], dp[curr_index - offer_index] + offer_price)

        return dp[-1]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p638.json').test_cases

        for case in cases:
            actual = Solution().shoppingOffers(case.price, case.special, case.needs)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
