import unittest
import utils


def compute_index(sizes):
    index = 0
    for size in sizes:
        index = (index << 3) | size
    return index


def iter_sizes(lo, hi):
    if all(lo[i] <= hi[i] for i in range(len(lo))):
        sizes = list(lo)
        yield sizes

        last = len(lo) - 1
        i = last

        while i >= 0:
            if sizes[i] == hi[i]:
                sizes[i] = lo[i]
                i -= 1
            else:
                sizes[i] += 1
                i = last
                yield sizes


# O(n*m^n) time. O(2^(3*m)) space. Space-optimized DP.
class Solution:
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        n = len(price)
        dp = [0] * (compute_index(needs) + 1)

        for sizes in iter_sizes([0] * n, needs):
            market_price = sum(price[i] * sizes[i] for i in range(n))
            dp[compute_index(sizes)] = market_price

        for offer in special:
            offer_price = offer[-1]
            market_price = sum(price[i] * offer[i] for i in range(n))
            if market_price <= offer_price:
                continue

            offer_sizes = offer[:-1]
            offer_index = compute_index(offer_sizes)

            for sizes in iter_sizes(offer_sizes, needs):
                curr_index = compute_index(sizes)
                dp[curr_index] = min(dp[curr_index], dp[curr_index - offer_index] + offer_price)

        return dp[-1]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().shoppingOffers(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
