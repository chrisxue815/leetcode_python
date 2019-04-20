import unittest
import utils


# DFS.
class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        n = len(price)

        def market_price(sizes):
            return sum(price[i] * sizes[i] for i in range(n))

        def not_overbuying(a, b):
            return all(a[i] <= b[i] for i in range(n))

        special = [offer for offer in special
                   if offer[-1] < market_price(offer) and not_overbuying(offer, needs)]

        def add_to_needs(sizes):
            for i in range(n):
                needs[i] += sizes[i]

        def remove_from_needs(sizes):
            for i in range(n):
                needs[i] -= sizes[i]

                if needs[i] < 0:
                    # Revert
                    for i in range(i + 1):
                        needs[i] += sizes[i]
                    return False

            return True

        def dfs(start, prev_cost):
            min_cost = prev_cost + market_price(needs)

            for i in range(start, len(special)):
                offer = special[i]

                if remove_from_needs(offer):
                    curr_cost = prev_cost + offer[-1]
                    min_cost = min(min_cost, dfs(i, curr_cost))

                    add_to_needs(offer)

            return min_cost

        return dfs(0, 0)


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().shoppingOffers(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
